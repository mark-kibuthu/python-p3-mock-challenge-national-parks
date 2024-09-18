import pytest

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip

class TestTrip:
    """Trip in many_to_many.py"""

    def test_has_start_date(self):
        """Trip is initialized with a start_date"""
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip_1 = Trip(matteo, yosemite, "May 5th", "May 9th")
        trip_2 = Trip(matteo, yosemite, "May 20th", "May 27th")

        assert trip_1.start_date == "May 5th"
        assert trip_2.start_date == "May 20th"

    def test_start_date_is_mutable_string(self):
        """Trip is initialized with a mutable start_date of type str"""
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")

        assert isinstance(trip.start_date, str)

        # Test mutation of start_date with valid string
        trip.start_date = "May 6th"
        assert trip.start_date == "May 6th"

        # Ensure exception is raised for invalid types
        with pytest.raises(TypeError):
            trip.start_date = 2

    def test_start_date_has_valid_length(self):
        """Trip start_date has valid length"""
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")

        # Ensure exception is raised for invalid length
        with pytest.raises(ValueError):
            Trip(matteo, yosemite, "May5th", "May 9th")

    def test_has_end_date(self):
        """Trip is initialized with an end_date"""
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")

        assert trip.end_date == "May 9th"

    def test_end_date_is_mutable_string(self):
        """Trip is initialized with a mutable end_date of type str"""
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")

        assert isinstance(trip.end_date, str)

        # Test mutation of end_date with valid string
        trip.end_date = "May 10th"
        assert trip.end_date == "May 10th"

        # Ensure exception is raised for invalid types
        with pytest.raises(TypeError):
            trip.end_date = 2

    def test_end_date_has_valid_length(self):
        """Trip end_date has valid length"""
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")

        # Ensure exception is raised for invalid length
        with pytest.raises(ValueError):
            Trip(matteo, yosemite, "May 5th", "May8th")

    def test_has_visitor(self):
        """Trip is initialized with a visitor"""
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        mark = Visitor("Mark")
        trip_1 = Trip(matteo, yosemite, "May 5th", "May 9th")
        trip_2 = Trip(mark, yosemite, "May 20th", "May 27th")

        assert trip_1.visitor == matteo
        assert trip_2.visitor == mark

    def test_visitor_of_type_visitor(self):
        """Trip visitor is of type Visitor"""
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        mark = Visitor("Mark")
        trip_1 = Trip(matteo, yosemite, "May 5th", "May 9th")
        trip_2 = Trip(mark, yosemite, "May 20th", "May 27th")

        assert isinstance(trip_1.visitor, Visitor)
        assert isinstance(trip_2.visitor, Visitor)

    def test_has_national_park(self):
        """Trip is initialized with a national_park"""
        yosemite = NationalPark("Yosemite")
        rocky_mountain = NationalPark("Rocky Mountain")
        matteo = Visitor("Matteo")
        trip_1 = Trip(matteo, yosemite, "May 5th", "May 9th")
        trip_2 = Trip(matteo, rocky_mountain, "May 20th", "May 27th")

        assert trip_1.national_park == yosemite
        assert trip_2.national_park == rocky_mountain

    def test_national_park_of_type_national_park(self):
        """Trip national_park is of type NationalPark"""
        yosemite = NationalPark("Yosemite")
        rocky_mountain = NationalPark("Rocky Mountain")
        matteo = Visitor("Matteo")
        trip_1 = Trip(matteo, yosemite, "May 5th", "May 9th")
        trip_2 = Trip(matteo, rocky_mountain, "May 20th", "May 27th")

        assert isinstance(trip_1.national_park, NationalPark)
        assert isinstance(trip_2.national_park, NationalPark)

    def test_get_all_trips(self):
        """Trip class has all_trips attribute"""
        Trip.all_trips = []
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        john = Visitor("John")
        trip_1 = Trip(matteo, yosemite, "May 5th", "May 9th")
        trip_2 = Trip(john, yosemite, "May 20th", "May 27th")

        assert len(Trip.all_trips) == 2
        assert trip_1 in Trip.all_trips
        assert trip_2 in Trip.all_trips
