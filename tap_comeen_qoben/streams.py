"""Stream type classes for tap-comeen-qoben."""

from __future__ import annotations

from singer_sdk import typing as th

from tap_comeen_qoben.client import ComeenQobenStream


class ContactsStream(ComeenQobenStream):
    """Contacts stream from the Comeen Qoben API."""

    name = "contacts"
    path = "/contacts"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("customerId", th.StringType),
        th.Property("email", th.StringType),
        th.Property("firstName", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("organizationName", th.StringType),
        th.Property(
            "address",
            th.ObjectType(
                th.Property("address1", th.StringType),
                th.Property("address2", th.StringType),
                th.Property("address3", th.StringType),
                th.Property("city", th.StringType),
                th.Property("country", th.StringType),
                th.Property("postalCode", th.StringType),
                th.Property("state", th.StringType),
            )
        ),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
    ).to_dict()


class CouponsStream(ComeenQobenStream):
    """Coupons stream from the Comeen Qoben API."""

    name = "coupons"
    path = "/coupons"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("percentOff", th.IntegerType),
        th.Property("productIds", th.ArrayType(th.StringType)),
        th.Property("status", th.StringType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
    ).to_dict()


class CustomersStream(ComeenQobenStream):
    """Customers stream from the Comeen Qoben API."""

    name = "customers"
    path = "/customers"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("status", th.StringType),
        th.Property("taxExempt", th.BooleanType),
        th.Property("ccEmails", th.ArrayType(th.StringType)),
        th.Property("email", th.StringType),
        th.Property("firstName", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("organizationName", th.StringType),
        th.Property("organizationVatNumber", th.StringType),
        th.Property("preferredLocale", th.StringType),
        th.Property(
            "billingContact",
            th.ObjectType(
                th.Property("id", th.StringType),
            ),
        ),
        th.Property(
            "hierarchy",
            th.ObjectType(
                th.Property("id", th.StringType),
            )
        ),
        th.Property(
            "invoiceSettings",
            th.ObjectType(
                th.Property("isConsolidationEnabled", th.BooleanType),
                th.Property("daysUntilPaymentDue", th.IntegerType),
                th.Property("purchaseOrder", th.StringType),
            ),
        ),
        th.Property(
            "metadata",
            th.ObjectType(
                th.Property("cf_client_group", th.StringType),
                th.Property("cf_type", th.StringType),
            ),
        ),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
    ).to_dict()


class DiscountsStream(ComeenQobenStream):
    """Discounts stream from the Comeen Qoben API."""

    name = "discounts"
    path = "/discounts"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("couponId", th.StringType),
        th.Property("subscriptionId", th.StringType),
        th.Property("name", th.StringType),
        th.Property("appliedOn", th.StringType),
        th.Property("occurrences", th.IntegerType),
        th.Property("percentOff", th.IntegerType),
        th.Property("startAt", th.DateTimeType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
    ).to_dict()


class HierarchiesStream(ComeenQobenStream):
    """Hierarchies stream from the Comeen Qoben API."""

    name = "hierarchies"
    path = "/hierarchies"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("billTo", th.StringType),
        th.Property("parentId", th.StringType),
        th.Property("customerId", th.StringType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
    ).to_dict()


class PricesStream(ComeenQobenStream):
    """Prices stream from the Comeen Qoben API."""

    name = "prices"
    path = "/prices"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("productId", th.StringType),
        th.Property("taxMode", th.StringType),
        th.Property("type", th.StringType),
        th.Property("usage", th.StringType),
        th.Property("recurring", th.ObjectType(
            th.Property("billingTime", th.StringType),
            th.Property("intervalCount", th.IntegerType),
            th.Property("intervalType", th.StringType)
        )),
        th.Property("unitPrices", th.ArrayType(
            th.ObjectType(
                th.Property("unitAmount", th.DecimalType),
                th.Property("currencyCode", th.StringType)
            )
        )),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
    ).to_dict()


class ProductsStream(ComeenQobenStream):
    """Products stream from the Comeen Qoben API."""

    name = "products"
    path = "/products"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("name", th.StringType),
        th.Property("description", th.StringType),
        th.Property("prices", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.StringType),
            )
        )),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
    ).to_dict()


class SubscriptionsStream(ComeenQobenStream):
    """Subscriptions stream from the Comeen Qoben API."""

    name = "subscriptions"
    path = "/subscriptions"
    primary_keys = ("id",)
    replication_key = None

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("discounts", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.StringType),
            )
        )),
        th.Property("metadata", th.ObjectType(
            th.Property("cf_client_name", th.StringType),
            th.Property("cf_sub_cancel_reason", th.StringType),
            th.Property("cf_sales", th.StringType),
            th.Property("cf_client_group_sub", th.StringType),
        )),
        th.Property("subscriptionItems", th.ArrayType(
            th.ObjectType(
                th.Property("id", th.StringType),
                th.Property("createdAt", th.DateTimeType),
                th.Property("updatedAt", th.DateTimeType),
                th.Property("billedPeriodEndAt", th.DateTimeType),
                th.Property("billedPeriodStartAt", th.DateTimeType),
                th.Property("discounts", th.ArrayType(
                    th.ObjectType(
                        th.Property("id", th.StringType),
                    )
                )),
                
                th.Property("name", th.StringType),
                th.Property("nextBillingAt", th.DateTimeType),
                th.Property("offerId", th.StringType),
                th.Property("offerItemId", th.StringType),
                th.Property("productId", th.StringType),
                th.Property("endAt", th.DateTimeType),
                th.Property("startAt", th.DateTimeType),
               	th.Property("price", th.ObjectType(
                   	th.Property("currencyCode", th.StringType),
                   	th.Property("recurring", th.ObjectType(
                       	th.Property("billingTime", th.StringType),
                       	th.Property("intervalCount", th.IntegerType),
                       	th.Property("intervalType", th.StringType)
                   	)),
                   	th.Property("taxMode", th.StringType),
                   	th.Property("type", th.StringType),
                    th.Property("unitAmount", th.DecimalType),
                    th.Property("id", th.StringType)
                )),
               th.Property("quantity", th.IntegerType),
               th.Property("quantityThreshold", th.IntegerType),
               th.Property("status", th.StringType)
            )
        )),
        th.Property("customer", th.ObjectType(
            th.Property("id", th.StringType),
        )),
        th.Property("invoiceSettings", th.ObjectType(
            th.Property("daysUntilPaymentDue", th.IntegerType),
            th.Property("purchaseOrder", th.StringType),
        )),
        th.Property("paymentSettings", th.ObjectType(
            th.Property("autoCollection", th.BooleanType),
        )),
        th.Property("reference", th.StringType),
        th.Property("status", th.StringType),
        th.Property("startAt", th.DateTimeType),
        th.Property("endAt", th.DateTimeType),
        th.Property("goLiveAt", th.DateTimeType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
    ).to_dict()
