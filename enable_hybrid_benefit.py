from azure.identity import AzureCliCredential
from azure.mgmt.compute import ComputeManagementClient
import sys

def enable_azure_hybrid_benefit(subscription_id, resource_group, vm_name):
    # Use Azure CLI authentication
    credential = AzureCliCredential()
    compute_client = ComputeManagementClient(credential, subscription_id)

    print(f"Fetching VM: {vm_name} in resource group: {resource_group}...")

    # Get current VM state
    vm = compute_client.virtual_machines.get(resource_group, vm_name)

    print(f"Current licenseType: {vm.license_type}")
    
    # Set the licenseType to Windows_Server (Azure Hybrid Benefit)
    vm.license_type = "Windows_Server"

    print(f"Updating VM: {vm_name} to enable Azure Hybrid Benefit...")
    poller = compute_client.virtual_machines.begin_create_or_update(resource_group, vm_name, vm)
    result = poller.result()

    print(f"Update complete. New licenseType: {result.license_type}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python enable_hybrid_benefit.py <subscription_id> <resource_group> <vm_name>")
        sys.exit(1)

    subscription_id = sys.argv[1]
    resource_group = sys.argv[2]
    vm_name = sys.argv[3]

    enable_azure_hybrid_benefit(subscription_id, resource_group, vm_name)
