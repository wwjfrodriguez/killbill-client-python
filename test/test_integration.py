# coding: utf-8

#
# Copyright 2014-2017 Groupon, Inc.
# Copyright 2014-2017 The Billing Project, LLC
#
# The Billing Project, LLC licenses this file to you under the Apache License, version 2.0
# (the "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 1.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import killbill
from killbill.models.account import Account
from killbill.models.tenant import Tenant
from killbill.models.payment_method import PaymentMethod
from killbill.models.subscription import Subscription
from killbill.models.invoice_dry_run import InvoiceDryRun
from killbill.models.invoice_item import InvoiceItem
from killbill.models.payment_transaction import PaymentTransaction
from random import choice
from string import ascii_lowercase
import time
from killbill.rest import ApiException


class TestIntegration(unittest.TestCase):
    """Account unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_integration(self):
        # Create tenant
        random_api_key = ''.join(choice(ascii_lowercase) for i in range(4))
        random_api_secret = ''.join(choice(ascii_lowercase) for i in range(5))
        tenant = killbill.api.TenantApi()
        body = Tenant(api_key=random_api_key, api_secret=random_api_secret)
        tenant.create_tenant(body, 'test')

        # Set api_key and api_secret
        kb_conf = killbill.configuration.Configuration()
        kb_conf.api_key['X-Killbill-ApiKey'] = random_api_key
        kb_conf.api_key['X-Killbill-ApiSecret'] = random_api_secret

        # Get tenant
        tenant = killbill.api.TenantApi()
        tenant = tenant.get_tenant_by_api_key(api_key=random_api_key)
        self.assertIsNotNone(tenant.tenant_id)
        self.assertEqual(random_api_key, tenant.api_key)

        # Upload XML catalog/Fetch XML catalog
        catalog = killbill.api.CatalogApi()
        xml_catalog = open("../resources/SpyCarBasic.xml", "r+").read()
        catalog.upload_catalog_xml(xml_catalog, 'test')

        # Get catalog
        catalog = killbill.api.CatalogApi()
        catalog = catalog.get_catalog_xml()
        self.assertIsNotNone(catalog)

        # Create account
        account = killbill.api.AccountApi()
        random_external_key = ''.join(choice(ascii_lowercase) for i in range(6))
        body = Account(name='John', external_key=random_external_key, currency='USD', state='CA', country='USA')
        account.create_account(body, 'test')
        #
        # Get account
        account = killbill.api.AccountApi()
        account = account.get_account_by_key(random_external_key)
        account_id = account.account_id
        self.assertIsNotNone(account.account_id)
        self.assertEqual(random_external_key, account.external_key)
        self.assertEqual('John', account.name)
        self.assertEqual('USD', account.currency)
        self.assertEqual('CA', account.state)
        self.assertEqual('USA', account.country)


        # Add a payment method
        account = killbill.api.AccountApi()
        body = PaymentMethod(plugin_name='__EXTERNAL_PAYMENT__', plugin_info=None)
        account.create_payment_method(account_id, body, 'test')

        # Get a payment method
        account = killbill.api.AccountApi()
        payment_method = account.get_payment_methods_for_account(account_id)
        self.assertIsNotNone(payment_method[0].payment_method_id)
        self.assertEqual(account_id, payment_method[0].account_id)
        self.assertEqual('__EXTERNAL_PAYMENT__', payment_method[0].plugin_name)

        # Tag account as AUTO_INVOICING_OFF
        account = killbill.api.AccountApi()
        tag = ["00000000-0000-0000-0000-000000000002"]
        account.create_account_tags(account_id, tag, 'test')

        # Get account tags
        tags = account.get_account_tags(account_id)
        self.assertIsNotNone(tags[0].tag_id)
        self.assertEqual("00000000-0000-0000-0000-000000000002", tags[0].tag_definition_id)
        self.assertEqual("AUTO_INVOICING_OFF", tags[0].tag_definition_name)

        # Create a subscription against plan
        subscription = killbill.api.SubscriptionApi()
        body = Subscription(account_id=account_id, plan_name='standard-monthly')
        subscription.create_subscription(body, 'test')

        # Get account bundles
        account = killbill.api.AccountApi()
        bundles = account.get_account_bundles(account_id)
        subscription_id = bundles[0].subscriptions[0].subscription_id

        # Get subscription
        subscription = killbill.api.SubscriptionApi()
        subscription = subscription.get_subscription(subscription_id)
        self.assertEqual('standard-monthly', subscription.plan_name)

        time.sleep(.5)

        # Get account invoices
        account = killbill.api.AccountApi()
        invoices = account.get_invoices_for_account(account_id)
        self.assertEqual([], invoices)

        # Remove AUTO_INVOICING_OFF tag
        account = killbill.api.AccountApi()
        account.delete_account_tags(account_id, 'test', tag_def=tag)

        time.sleep(.5)

        # Get account invoices
        account = killbill.api.AccountApi()
        invoices = account.get_invoices_for_account(account_id)
        self.assertIsNotNone(invoices[0].invoice_id)

        # Create a dryRun invoice
        invoice = killbill.api.InvoiceApi()
        body = InvoiceDryRun(dry_run_type='TARGET_DATE')
        invoice.generate_dry_run_invoice(body, account_id, 'test')

        # Modify Plan
        subscription = killbill.api.SubscriptionApi()
        body = Subscription(subscription_id=subscription_id, product_name='Sports', billing_period='MONTHLY',
                            price_list='DEFAULT')
        subscription.change_subscription_plan(subscription_id, body, 'test', billing_policy='IMMEDIATE')

        # Create external charge
        invoice = killbill.api.InvoiceApi()
        body = InvoiceItem(account_id=account_id, amount=50, currency='USD', description='My charge')
        invoice.create_external_charges(account_id, [body], 'test', auto_commit=True)

        # Verify account balance
        account = killbill.api.AccountApi()
        account = account.get_account(account_id, account_with_balance=True)
        self.assertEqual(50.0, account.account_balance)

        # Pay all unpaid invoices
        account = killbill.api.AccountApi()
        account.pay_all_invoices(account_id, 'test', external_payment=True)

        # Verify account balance
        account = killbill.api.AccountApi()
        account = account.get_account(account_id, account_with_balance=True)
        self.assertEqual(0, account.account_balance)

        # Get account invoice payments
        account = killbill.api.AccountApi()
        invoice_payments = account.get_invoice_payments(account_id)
        payment_id = invoice_payments[0].transactions[0].payment_id
        self.assertEqual(1, len(invoice_payments[0].transactions))

        # Create a refund
        payment = killbill.api.PaymentApi()
        body = PaymentTransaction(payment_id=payment_id, amount=50)
        payment.refund_payment(payment_id, body, 'test')

        # Get account invoice payments
        account = killbill.api.AccountApi()
        invoice_payments = account.get_invoice_payments(account_id)
        self.assertEqual(2, len(invoice_payments[0].transactions))
        self.assertEqual('REFUND', invoice_payments[0].transactions[1].transaction_type)

        # Cancel subscription
        subscription = killbill.api.SubscriptionApi()
        subscription.cancel_subscription_plan(subscription_id, 'test')

        # Get subscription
        subscription = killbill.api.SubscriptionApi()
        subscription = subscription.get_subscription(subscription_id)
        self.assertEqual('CANCELLED', subscription.state)

        pass

    def test_pagination_and_search(self):
        # Create tenant
        random_api_key = ''.join(choice(ascii_lowercase) for i in range(4))
        random_api_secret = ''.join(choice(ascii_lowercase) for i in range(5))

        # Set api_key and api_secret
        kb_conf = killbill.configuration.Configuration()
        kb_conf.api_key['X-Killbill-ApiKey'] = random_api_key
        kb_conf.api_key['X-Killbill-ApiSecret'] = random_api_secret

        tenant = killbill.api.TenantApi()
        body = Tenant(api_key=random_api_key, api_secret=random_api_secret)
        tenant.create_tenant(body, 'test')

        # Create 10 accounts with payment methods and external charges
        for x in range(0, 10):
            account = killbill.api.AccountApi()
            random_external_key = ''.join(choice(ascii_lowercase) for i in range(6))
            body = Account(name='John-' + str(x), external_key=random_external_key, currency='USD', state='CA',
                           country='USA')
            account.create_account(body, 'test')

            # Get account
            account = killbill.api.AccountApi()
            account = account.get_account_by_key(random_external_key)
            account_id = account.account_id

            # Add a payment method
            account = killbill.api.AccountApi()
            body = PaymentMethod(plugin_name='__EXTERNAL_PAYMENT__', plugin_info=None)
            account.create_payment_method(account_id, body, 'test')

            # Create external charges
            invoice = killbill.api.InvoiceApi()
            body = InvoiceItem(account_id=account_id, amount=50, currency='USD', description='My charge')
            invoice.create_external_charges(account_id, [body], 'test', auto_commit=True)

            # Pay all unpaid invoices
            account = killbill.api.AccountApi()
            account.pay_all_invoices(account_id, 'test', external_payment=True)

        # Pagination list accounts
        account = killbill.api.AccountApi()
        accounts = account.get_accounts()
        self.assertEqual(10, len(accounts))

        # Pagination list invoice
        invoice = killbill.api.InvoiceApi()
        invoices = invoice.get_invoices()
        self.assertEqual(10, len(invoices))

        # Pagination list payments
        payment = killbill.api.PaymentApi()
        payments = payment.get_payments()
        self.assertEqual(10, len(payments))

        # Search accounts
        account = killbill.api.AccountApi()
        accounts = account.search_accounts('John-1')
        self.assertEqual(1, len(accounts))

        # Search payments
        payment = killbill.api.PaymentApi()
        payments = payment.search_payments('SUCCESS')
        self.assertEqual(10, len(payments))

        # Search invoices
        invoice = killbill.api.InvoiceApi()
        invoices = invoice.search_invoices('USD')
        self.assertEqual(10, len(invoices))

        pass


if __name__ == '__main__':
    unittest.main()