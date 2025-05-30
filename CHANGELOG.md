# Changelog

All notable changes to this project will be documented in this file.

## [0.0.4] - 2025-01-XX

### Added
- **Permission System**: Added granular permission controls for CRUD operations
  - `ODOO_PERMISSION_READ`: Control read operations (default: enabled)
  - `ODOO_PERMISSION_WRITE`: Control write operations (default: enabled)
  - `ODOO_PERMISSION_UPDATE`: Control update operations (default: enabled)
  - `ODOO_PERMISSION_DELETE`: Control delete operations (default: disabled)
- Automatic method classification into operation types (read/write/update/delete)
- Permission checking in all tools and resources
- Enhanced error handling with permission-specific error messages
- Updated documentation with permission configuration examples

### Changed
- All operations now check permissions before execution
- Error responses include error type information for permission errors
- Default configuration disables delete operations for safety

## [0.0.3] - 2025-03-18

### Fixed
- Fixed `OdooClient` class by adding missing methods: `get_models()`, `get_model_info()`, `get_model_fields()`, `search_read()`, and `read_records()`
- Ensured compatibility with different Odoo versions by using only basic fields when retrieving model information

### Added
- Support for retrieving all models from an Odoo instance
- Support for retrieving detailed information about specific models
- Support for searching and reading records with various filtering options

## [0.0.2] - 2025-03-18

### Fixed
- Added missing dependencies in pyproject.toml: `mcp>=0.1.1`, `requests>=2.31.0`, `xmlrpc>=0.4.1`

## [0.0.1] - 2025-03-18

### Added
- Initial release with basic Odoo XML-RPC client support
- MCP Server integration for Odoo
- Command-line interface for quick setup and testing 