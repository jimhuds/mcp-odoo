#!/usr/bin/env python3
"""
Test script for the Odoo MCP Server permission system
"""

import os
import sys
import subprocess
import json

def test_permissions():
    """Test the permission system with different configurations"""
    
    print("Testing Odoo MCP Server Permission System")
    print("=" * 50)
    
    # Test configurations
    test_configs = [
        {
            "name": "Read-only mode",
            "env": {
                "ODOO_PERMISSION_READ": "1",
                "ODOO_PERMISSION_WRITE": "0", 
                "ODOO_PERMISSION_UPDATE": "0",
                "ODOO_PERMISSION_DELETE": "0"
            }
        },
        {
            "name": "Write-only mode",
            "env": {
                "ODOO_PERMISSION_READ": "0",
                "ODOO_PERMISSION_WRITE": "1",
                "ODOO_PERMISSION_UPDATE": "0", 
                "ODOO_PERMISSION_DELETE": "0"
            }
        },
        {
            "name": "Full permissions",
            "env": {
                "ODOO_PERMISSION_READ": "1",
                "ODOO_PERMISSION_WRITE": "1",
                "ODOO_PERMISSION_UPDATE": "1",
                "ODOO_PERMISSION_DELETE": "1"
            }
        },
        {
            "name": "No permissions",
            "env": {
                "ODOO_PERMISSION_READ": "0",
                "ODOO_PERMISSION_WRITE": "0",
                "ODOO_PERMISSION_UPDATE": "0",
                "ODOO_PERMISSION_DELETE": "0"
            }
        }
    ]
    
    for config in test_configs:
        print(f"\n{config['name']}:")
        print("-" * 30)
        
        # Show environment variables
        for key, value in config['env'].items():
            print(f"  {key}={value}")
        
        # Show expected behavior
        permissions = config['env']
        print("\nExpected behavior:")
        print(f"  Read operations: {'✓' if permissions['ODOO_PERMISSION_READ'] == '1' else '✗'}")
        print(f"  Write operations: {'✓' if permissions['ODOO_PERMISSION_WRITE'] == '1' else '✗'}")
        print(f"  Update operations: {'✓' if permissions['ODOO_PERMISSION_UPDATE'] == '1' else '✗'}")
        print(f"  Delete operations: {'✓' if permissions['ODOO_PERMISSION_DELETE'] == '1' else '✗'}")


if __name__ == "__main__":
    test_permissions()
    
    print("\n" + "=" * 50)
    print("To test with actual Odoo connection:")
    print("1. Set your Odoo connection environment variables:")
    print("   export ODOO_URL='https://your-odoo-instance.com'")
    print("   export ODOO_DB='your-database'")
    print("   export ODOO_USERNAME='your-username'")
    print("   export ODOO_PASSWORD='your-password'")
    print("")
    print("2. Set permission variables and run the server:")
    print("   export ODOO_PERMISSION_READ='1'")
    print("   export ODOO_PERMISSION_WRITE='0'")
    print("   export ODOO_PERMISSION_UPDATE='0'")
    print("   export ODOO_PERMISSION_DELETE='0'")
    print("   python -m odoo_mcp")
    print("")
    print("3. Use the check_permissions tool to verify configuration") 