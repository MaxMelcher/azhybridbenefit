# Azure Hybrid Benefit Management Tool

This Python script enables Azure Hybrid Benefit for Windows Server virtual machines in Azure, allowing you to use your on-premises Windows Server licenses in the cloud and reduce costs.

## What is Azure Hybrid Benefit?

Azure Hybrid Benefit is a licensing benefit that helps you reduce the costs of running your workloads in the cloud. It allows you to use your on-premises Software Assurance-enabled Windows Server licenses on Azure VMs, paying only for the base compute cost.

## Prerequisites

- Python 3.10 or higher
- Azure CLI installed and authenticated (`az login`)
- Required Python packages (install with `pip install -r requirements.txt`)
- Contributor permissions to modify virtual machines in the provided Azure subscription.

## Installation

1. Clone this repository or download the script
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you're logged in to Azure CLI:

   ```bash
   az login
   ```

## Usage

The script takes three required parameters:

- `subscription_id`: Your Azure subscription ID
- `resource_group`: The resource group containing the VM
- `vm_name`: The name of the virtual machine

### Basic Usage

```bash
python enable_hybrid_benefit.py <subscription_id> <resource_group> <vm_name>
```

### Example

```bash
python enable_hybrid_benefit.py 568aee08-3760-4b25-a6a5-087028e0726c hybrid test
```

This command will:

1. Connect to Azure using your CLI credentials
2. Fetch the specified VM from the resource group
3. Display the current license type
4. Update the VM to enable Azure Hybrid Benefit (set `licenseType` to `Windows_Server`)
5. Confirm the update was successful

## What the Script Does

1. **Authentication**: Uses Azure CLI credentials for authentication
2. **VM Retrieval**: Fetches the current state of the specified VM
3. **License Update**: Changes the `licenseType` property to `Windows_Server`
4. **Verification**: Confirms the change was applied successfully

## Important Notes

- This script is specifically for Windows Server VMs
- Ensure you have the proper Windows Server licenses with Software Assurance
- The change may take a few minutes to complete

## Error Handling

If you encounter authentication issues, make sure you're logged in to Azure CLI:

```bash
az login
az account show  # Verify you're logged in to the correct subscription
```

## License

This project is licensed under the terms specified in the LICENSE file.