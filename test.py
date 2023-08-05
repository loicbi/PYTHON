from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential

# Get the password
keyVaultName = 'DataHubCanadaKeyVault'
KVUri = f"https://datahubcanadakeyvault.vault.azure.net"

credentials = ClientSecretCredential(
    client_id="b1ca00d4-756a-43da-ba54-3475b5221239",
    client_secret="niA8Q~ahIZlRgRQhrOQ-HwKgSS2mjswhYMirdcLY",
    tenant_id="da67ef1b-ca59-4db2-9a8c-aa8d94617a16"
)
secret_client = SecretClient(vault_url=KVUri, credential=credentials)
secret = secret_client.get_secret('org-gs1ca-core-blob')
secret_connection_string = secret.value

print(secret_connection_string)

# context.updateVariable('jv_pwd_scotts', jv_pwd_scotts)
