class NationalPark:
    all_parks = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("NationalPark name must be a string with at least 3 characters.")
        self._name = name
        NationalPark.all_parks.append(self)

    @property
    def name(self):
        return self._name

    def trips(self):
        # Return all trips that include this park
        return [trip for trip in Trip.all_trips if trip.national_park == self]

    def visitors(self):
        # Return unique visitors who visited the park
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        # Return the total number of visits to this park
        return len(self.trips())

    def best_visitor(self):
        # Return the visitor who visited this park the most
        if not self.trips():
            return None
        visit_count = {}
        for trip in self.trips():
            if trip.visitor not in visit_count:
                visit_count[trip.visitor] = 0
            visit_count[trip.visitor] += 1
        return max(visit_count, key=visit_count.get)
class Trip:
    all_trips = []

    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(start_date, str) or len(start_date) < 7:
            raise ValueError("Start date must be a string and at least 7 characters long.")
        if not isinstance(end_date, str) or len(end_date) < 7:
            raise ValueError("End date must be a string and at least 7 characters long.")
        if not isinstance(visitor, Visitor):
            raise ValueError("Visitor must be of type Visitor.")
        if not isinstance(national_park, NationalPark):
            raise ValueError("NationalPark must be of type NationalPark.")
        
        self._start_date = start_date
        self._end_date = end_date
        self.visitor = visitor
        self.national_park = national_park
        Trip.all_trips.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str):
            raise TypeError("start_date must be a string")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str):
            raise TypeError("end_date must be a string")
        self._end_date = value
class Visitor:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Visitor name must be a string between 1 and 15 characters.")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("name must be between 1 and 15 characters")
        self._name = value

    def trips(self):
        # Return all trips for this visitor
        return [trip for trip in Trip.all_trips if trip.visitor == self]

    def national_parks(self):
        # Return a list of unique parks this visitor has visited
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        # Return the number of times the visitor visited a specific park
        return len([trip for trip in self.trips() if trip.national_park == park])
