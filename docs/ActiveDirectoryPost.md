# ActiveDirectoryPost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computer_name** | **str** | The common name of the computer account to be created in the Active Directory domain. If not specified, defaults to the name of the Active Directory configuration. | [optional] 
**directory_servers** | **list[str]** | A list of directory servers that will be used for lookups related to user authorization. Accepted server formats are IP address and DNS name. All specified servers must be registered to the domain appropriately in the array&#39;s configured DNS and will only be communicated with over the secure LDAP (LDAPS) protocol. If not specified, servers are resolved for the domain in DNS. The specified list can have a maximum length of 5. | [optional] 
**domain** | **str** | The Active Directory domain to join. | 
**encryption_types** | **list[str]** | The encryption types that will be supported for use by clients for Kerberos authentication. Defaults to &#x60;aes256-cts-hmac-sha1-96&#x60;. Valid values include &#x60;aes256-cts-hmac-sha1-96&#x60;, &#x60;aes128-cts-hmac-sha1-96&#x60;, and &#x60;arcfour-hmac&#x60;. Cannot be provided if using an existing machine account. | [optional] 
**fqdns** | **list[str]** | A list of fully qualified domain names to use to register service principal names for the machine account. If specified, every service principal that is supported by the array will be registered for each fully qualified domain name specified. If neither &#x60;fqdns&#x60; nor &#x60;service_principal_names&#x60; is specified, the default &#x60;service_principal_names&#x60; are constructed using the &#x60;computer_name&#x60; and &#x60;domain&#x60; fields. Cannot be provided in combination with &#x60;service_principal_names&#x60;. Cannot be provided if using an existing machine account. | [optional] 
**join_ou** | **str** | The relative distinguished name of the organizational unit in which the computer account should be created when joining the domain. Cannot be provided if using an existing machine account. If not specified, defaults to &#x60;CN&#x3D;Computers&#x60;. | [optional] 
**kerberos_servers** | **list[str]** | A list of key distribution servers to use for Kerberos protocol. Accepted server formats are IP address and DNS name. All specified servers must be registered to the domain appropriately in the array&#39;s configured DNS. If not specified, servers are resolved for the domain in DNS. The specified list can have a maximum length of 5. | [optional] 
**password** | **str** | The login password of the user with privileges to create the computer account in the domain. If using an existing computer account, the user must have privileges to read attributes from the computer account and reset the password on that account. This is not persisted on the array. | 
**service_principal_names** | **list[str]** | A list of service principal names to register for the machine account, which can be used for the creation of keys for Kerberos authentication. If neither &#x60;service_principal_names&#x60; nor &#x60;fqdns&#x60; is specified, the default &#x60;service_principal_names&#x60; are constructed using the &#x60;computer_name&#x60; and &#x60;domain&#x60; fields. Cannot be provided in combination with &#x60;fqdns&#x60;. Cannot be provided if using an existing machine account. | [optional] 
**user** | **str** | The login name of the user with privileges to create the computer account in the domain. If using an existing computer account, the user must have privileges to read attributes from the computer account and reset the password on that account. This is not persisted on the array. | 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)

