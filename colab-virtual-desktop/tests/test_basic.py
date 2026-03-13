"""
Basic tests for colab-virtual-desktop package
"""

import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from colab_desktop import (
    ColabDesktop,
    is_colab,
    kill_processes_on_port,
    get_environment_summary
)


def test_imports():
    """Test that all modules can be imported"""
    assert ColabDesktop is not None
    assert callable(ColabDesktop)
    assert callable(is_colab)
    assert callable(kill_processes_on_port)
    assert callable(get_environment_summary)
    print("✅ All imports successful")


def test_colab_desktop_initialization():
    """Test ColabDesktop can be instantiated"""
    desktop = ColabDesktop(ngrok_auth_token="dummy_token_for_test")
    assert desktop is not None
    assert desktop.ngrok_auth_token == "dummy_token_for_test"
    assert desktop.vnc_password == "colab123"
    assert desktop.display == ":1"
    assert desktop.geometry == "1280x720"
    print("✅ ColabDesktop initialization OK")


def test_environment_summary():
    """Test environment summary generation"""
    summary = get_environment_summary()
    assert isinstance(summary, dict)
    assert 'is_colab' in summary
    assert 'python_version' in summary
    print(f"✅ Environment summary: {summary}")


def test_utils_functions():
    """Test utility functions"""
    # Test port kill (should not raise)
    kill_processes_on_port(99999)  # Non-existent port, should be safe
    print("✅ Utility functions OK")


def test_desktop_lifecycle():
    """Test desktop setup/start/stop lifecycle (without actually starting services)"""
    desktop = ColabDesktop(
        ngrok_auth_token="dummy",
        install_deps=False,  # Don't actually install
    )

    # Test that methods exist
    assert hasattr(desktop, 'setup')
    assert hasattr(desktop, 'start')
    assert hasattr(desktop, 'stop')
    assert hasattr(desktop, 'get_url')
    assert hasattr(desktop, 'restart')
    assert hasattr(desktop, 'log')

    print("✅ Desktop lifecycle methods present")


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("Running Colab Virtual Desktop Tests")
    print("=" * 60)

    tests = [
        test_imports,
        test_colab_desktop_initialization,
        test_environment_summary,
        test_utils_functions,
        test_desktop_lifecycle,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"❌ {test.__name__} failed: {e}")
            import traceback
            traceback.print_exc()
            failed += 1

    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
