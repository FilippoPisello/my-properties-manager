from pathlib import Path

# Paths to dir/items within the app folder
MODULE_ROOT_DIR = Path(__file__).parent.resolve()
DB_DIR = MODULE_ROOT_DIR / "database"

# Paths to dir/items outside of the app folder
PROJECT_ROOT_DIR = MODULE_ROOT_DIR.parent.resolve()
DB_INSTANCE_DIR = PROJECT_ROOT_DIR / "instance"
DB_INSTANCE_NAME = DB_INSTANCE_DIR / "my_app.sqlite"

# Test paths
TEST_DB_INSTANCE_NAME = DB_INSTANCE_DIR / "test_my_app.sqlite"
