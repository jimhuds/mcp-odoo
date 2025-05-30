#!/usr/bin/env python3
"""
Examples of using the Odoo MCP Server with different permission configurations
"""

import os

def setup_read_only_environment():
    """Setup environment for read-only access to Odoo"""
    print("Setting up READ-ONLY environment...")
    
    os.environ["ODOO_PERMISSION_READ"] = "1"
    os.environ["ODOO_PERMISSION_WRITE"] = "0"
    os.environ["ODOO_PERMISSION_UPDATE"] = "0"
    os.environ["ODOO_PERMISSION_DELETE"] = "0"
    
    print("✓ Read operations: ENABLED")
    print("✗ Write operations: DISABLED")
    print("✗ Update operations: DISABLED") 
    print("✗ Delete operations: DISABLED")
    print()
    print("Safe for: Reporting, data analysis, browsing records")
    print("Blocked: Creating, modifying, or deleting records")

def setup_data_entry_environment():
    """Setup environment for data entry (read and write only)"""
    print("Setting up DATA ENTRY environment...")
    
    os.environ["ODOO_PERMISSION_READ"] = "1"
    os.environ["ODOO_PERMISSION_WRITE"] = "1"
    os.environ["ODOO_PERMISSION_UPDATE"] = "0"
    os.environ["ODOO_PERMISSION_DELETE"] = "0"
    
    print("✓ Read operations: ENABLED")
    print("✓ Write operations: ENABLED")
    print("✗ Update operations: DISABLED")
    print("✗ Delete operations: DISABLED")
    print()
    print("Safe for: Creating new records, reading existing data")
    print("Blocked: Modifying or deleting existing records")

def setup_full_access_environment():
    """Setup environment for full access (use with caution)"""
    print("Setting up FULL ACCESS environment...")
    
    os.environ["ODOO_PERMISSION_READ"] = "1"
    os.environ["ODOO_PERMISSION_WRITE"] = "1"
    os.environ["ODOO_PERMISSION_UPDATE"] = "1"
    os.environ["ODOO_PERMISSION_DELETE"] = "1"
    
    print("✓ Read operations: ENABLED")
    print("✓ Write operations: ENABLED")
    print("✓ Update operations: ENABLED")
    print("⚠️  Delete operations: ENABLED")
    print()
    print("⚠️  WARNING: Full access enabled - use with extreme caution!")
    print("Allowed: All operations including data deletion")

def setup_no_access_environment():
    """Setup environment with no permissions (for testing)"""
    print("Setting up NO ACCESS environment...")
    
    os.environ["ODOO_PERMISSION_READ"] = "0"
    os.environ["ODOO_PERMISSION_WRITE"] = "0"
    os.environ["ODOO_PERMISSION_UPDATE"] = "0"
    os.environ["ODOO_PERMISSION_DELETE"] = "0"
    
    print("✗ Read operations: DISABLED")
    print("✗ Write operations: DISABLED")
    print("✗ Update operations: DISABLED")
    print("✗ Delete operations: DISABLED")
    print()
    print("Use case: Testing permission system, completely locked down")

if __name__ == "__main__":
    print("Odoo MCP Server Permission Examples")
    print("=" * 40)
    
    scenarios = [
        ("1", "Read-only (safe for reports)", setup_read_only_environment),
        ("2", "Data entry (read + write)", setup_data_entry_environment), 
        ("3", "Full access (DANGEROUS)", setup_full_access_environment),
        ("4", "No access (testing)", setup_no_access_environment)
    ]
    
    print("\nAvailable scenarios:")
    for num, desc, _ in scenarios:
        print(f"  {num}. {desc}")
    
    choice = input("\nSelect scenario (1-4): ").strip()
    
    for num, desc, setup_func in scenarios:
        if choice == num:
            print(f"\n{desc}")
            print("-" * len(desc))
            setup_func()
            print(f"\nEnvironment configured for: {desc}")
            print("Now run: python -m odoo_mcp")
            break
    else:
        print("Invalid choice. Please run again and select 1-4.") 