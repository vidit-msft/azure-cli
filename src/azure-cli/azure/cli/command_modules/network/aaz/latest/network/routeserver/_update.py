# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network routeserver update",
)
class Update(AAZCommand):
    """Update a route server.

    :example: Update a route server.
        az network routeserver update --name myrouteserver --resource-group myresourcegroup --allow-b2b-traffic
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/virtualhubs/{}", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the route server.",
            required=True,
            id_part="name",
        )
        _args_schema.allow_b2b_traffic = AAZBoolArg(
            options=["--allow-b2b-traffic"],
            help="Whether to allow branch to branch traffic.",
            nullable=True,
        )
        _args_schema.hub_routing_preference = AAZStrArg(
            options=["--hub-routing-preference"],
            help="Routing preference of the route server.",
            nullable=True,
            enum={"ASPath": "ASPath", "ExpressRoute": "ExpressRoute", "VpnGateway": "VpnGateway"},
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            help="Space-separated tags: key[=value] [key[=value] ...].",
            nullable=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        # define Arg Group "VirtualHubParameters"
        return cls._args_schema

    _args_sub_resource_update = None

    @classmethod
    def _build_args_sub_resource_update(cls, _schema):
        if cls._args_sub_resource_update is not None:
            _schema.id = cls._args_sub_resource_update.id
            return

        cls._args_sub_resource_update = AAZObjectArg(
            nullable=True,
        )

        sub_resource_update = cls._args_sub_resource_update
        sub_resource_update.id = AAZStrArg(
            options=["id"],
            help="Resource ID.",
            nullable=True,
        )

        _schema.id = cls._args_sub_resource_update.id

    def _execute_operations(self):
        self.pre_operations()
        self.VirtualHubsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.VirtualHubsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class VirtualHubsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualHubName", self.ctx.args.name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_virtual_hub_read(cls._schema_on_200)

            return cls._schema_on_200

    class VirtualHubsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualHubs/{virtualHubName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "virtualHubName", self.ctx.args.name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_virtual_hub_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("allowBranchToBranchTraffic", AAZBoolType, ".allow_b2b_traffic")
                properties.set_prop("hubRoutingPreference", AAZStrType, ".hub_routing_preference")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_sub_resource_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("id", AAZStrType, ".id")

    _schema_sub_resource_read = None

    @classmethod
    def _build_schema_sub_resource_read(cls, _schema):
        if cls._schema_sub_resource_read is not None:
            _schema.id = cls._schema_sub_resource_read.id
            return

        cls._schema_sub_resource_read = _schema_sub_resource_read = AAZObjectType()

        sub_resource_read = _schema_sub_resource_read
        sub_resource_read.id = AAZStrType()

        _schema.id = cls._schema_sub_resource_read.id

    _schema_virtual_hub_read = None

    @classmethod
    def _build_schema_virtual_hub_read(cls, _schema):
        if cls._schema_virtual_hub_read is not None:
            _schema.etag = cls._schema_virtual_hub_read.etag
            _schema.id = cls._schema_virtual_hub_read.id
            _schema.kind = cls._schema_virtual_hub_read.kind
            _schema.location = cls._schema_virtual_hub_read.location
            _schema.name = cls._schema_virtual_hub_read.name
            _schema.properties = cls._schema_virtual_hub_read.properties
            _schema.tags = cls._schema_virtual_hub_read.tags
            _schema.type = cls._schema_virtual_hub_read.type
            return

        cls._schema_virtual_hub_read = _schema_virtual_hub_read = AAZObjectType()

        virtual_hub_read = _schema_virtual_hub_read
        virtual_hub_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        virtual_hub_read.id = AAZStrType()
        virtual_hub_read.kind = AAZStrType(
            flags={"read_only": True},
        )
        virtual_hub_read.location = AAZStrType(
            flags={"required": True},
        )
        virtual_hub_read.name = AAZStrType(
            flags={"read_only": True},
        )
        virtual_hub_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        virtual_hub_read.tags = AAZDictType()
        virtual_hub_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_virtual_hub_read.properties
        properties.address_prefix = AAZStrType(
            serialized_name="addressPrefix",
        )
        properties.allow_branch_to_branch_traffic = AAZBoolType(
            serialized_name="allowBranchToBranchTraffic",
        )
        properties.azure_firewall = AAZObjectType(
            serialized_name="azureFirewall",
        )
        cls._build_schema_sub_resource_read(properties.azure_firewall)
        properties.bgp_connections = AAZListType(
            serialized_name="bgpConnections",
            flags={"read_only": True},
        )
        properties.express_route_gateway = AAZObjectType(
            serialized_name="expressRouteGateway",
        )
        cls._build_schema_sub_resource_read(properties.express_route_gateway)
        properties.hub_routing_preference = AAZStrType(
            serialized_name="hubRoutingPreference",
        )
        properties.ip_configurations = AAZListType(
            serialized_name="ipConfigurations",
            flags={"read_only": True},
        )
        properties.p2_s_vpn_gateway = AAZObjectType(
            serialized_name="p2SVpnGateway",
        )
        cls._build_schema_sub_resource_read(properties.p2_s_vpn_gateway)
        properties.preferred_routing_gateway = AAZStrType(
            serialized_name="preferredRoutingGateway",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.route_table = AAZObjectType(
            serialized_name="routeTable",
        )
        properties.routing_state = AAZStrType(
            serialized_name="routingState",
            flags={"read_only": True},
        )
        properties.security_partner_provider = AAZObjectType(
            serialized_name="securityPartnerProvider",
        )
        cls._build_schema_sub_resource_read(properties.security_partner_provider)
        properties.security_provider_name = AAZStrType(
            serialized_name="securityProviderName",
        )
        properties.sku = AAZStrType()
        properties.virtual_hub_route_table_v2s = AAZListType(
            serialized_name="virtualHubRouteTableV2s",
        )
        properties.virtual_router_asn = AAZIntType(
            serialized_name="virtualRouterAsn",
        )
        properties.virtual_router_auto_scale_configuration = AAZObjectType(
            serialized_name="virtualRouterAutoScaleConfiguration",
        )
        properties.virtual_router_ips = AAZListType(
            serialized_name="virtualRouterIps",
        )
        properties.virtual_wan = AAZObjectType(
            serialized_name="virtualWan",
        )
        cls._build_schema_sub_resource_read(properties.virtual_wan)
        properties.vpn_gateway = AAZObjectType(
            serialized_name="vpnGateway",
        )
        cls._build_schema_sub_resource_read(properties.vpn_gateway)

        bgp_connections = _schema_virtual_hub_read.properties.bgp_connections
        bgp_connections.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(bgp_connections.Element)

        ip_configurations = _schema_virtual_hub_read.properties.ip_configurations
        ip_configurations.Element = AAZObjectType()
        cls._build_schema_sub_resource_read(ip_configurations.Element)

        route_table = _schema_virtual_hub_read.properties.route_table
        route_table.routes = AAZListType()

        routes = _schema_virtual_hub_read.properties.route_table.routes
        routes.Element = AAZObjectType()

        _element = _schema_virtual_hub_read.properties.route_table.routes.Element
        _element.address_prefixes = AAZListType(
            serialized_name="addressPrefixes",
        )
        _element.next_hop_ip_address = AAZStrType(
            serialized_name="nextHopIpAddress",
        )

        address_prefixes = _schema_virtual_hub_read.properties.route_table.routes.Element.address_prefixes
        address_prefixes.Element = AAZStrType()

        virtual_hub_route_table_v2s = _schema_virtual_hub_read.properties.virtual_hub_route_table_v2s
        virtual_hub_route_table_v2s.Element = AAZObjectType()

        _element = _schema_virtual_hub_read.properties.virtual_hub_route_table_v2s.Element
        _element.etag = AAZStrType(
            flags={"read_only": True},
        )
        _element.id = AAZStrType()
        _element.name = AAZStrType()
        _element.properties = AAZObjectType(
            flags={"client_flatten": True},
        )

        properties = _schema_virtual_hub_read.properties.virtual_hub_route_table_v2s.Element.properties
        properties.attached_connections = AAZListType(
            serialized_name="attachedConnections",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.routes = AAZListType()

        attached_connections = _schema_virtual_hub_read.properties.virtual_hub_route_table_v2s.Element.properties.attached_connections
        attached_connections.Element = AAZStrType()

        routes = _schema_virtual_hub_read.properties.virtual_hub_route_table_v2s.Element.properties.routes
        routes.Element = AAZObjectType()

        _element = _schema_virtual_hub_read.properties.virtual_hub_route_table_v2s.Element.properties.routes.Element
        _element.destination_type = AAZStrType(
            serialized_name="destinationType",
        )
        _element.destinations = AAZListType()
        _element.next_hop_type = AAZStrType(
            serialized_name="nextHopType",
        )
        _element.next_hops = AAZListType(
            serialized_name="nextHops",
        )

        destinations = _schema_virtual_hub_read.properties.virtual_hub_route_table_v2s.Element.properties.routes.Element.destinations
        destinations.Element = AAZStrType()

        next_hops = _schema_virtual_hub_read.properties.virtual_hub_route_table_v2s.Element.properties.routes.Element.next_hops
        next_hops.Element = AAZStrType()

        virtual_router_auto_scale_configuration = _schema_virtual_hub_read.properties.virtual_router_auto_scale_configuration
        virtual_router_auto_scale_configuration.min_capacity = AAZIntType(
            serialized_name="minCapacity",
        )

        virtual_router_ips = _schema_virtual_hub_read.properties.virtual_router_ips
        virtual_router_ips.Element = AAZStrType()

        tags = _schema_virtual_hub_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_virtual_hub_read.etag
        _schema.id = cls._schema_virtual_hub_read.id
        _schema.kind = cls._schema_virtual_hub_read.kind
        _schema.location = cls._schema_virtual_hub_read.location
        _schema.name = cls._schema_virtual_hub_read.name
        _schema.properties = cls._schema_virtual_hub_read.properties
        _schema.tags = cls._schema_virtual_hub_read.tags
        _schema.type = cls._schema_virtual_hub_read.type


__all__ = ["Update"]
