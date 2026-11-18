from src.models import Apartment
from src.manager import Manager
from src.models import Parameters


def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key

def test_tenants_in_manager():
    parameters = Parameters()
    manager = Manager(parameters)

    expected_names = ["Jan Nowak", "Adam Kowalski", "Ewa Adamska"]

    assert len(manager.tenants) == len(expected_names)
    for tenant in manager.tenants.values():
        assert tenant.name in expected_names
