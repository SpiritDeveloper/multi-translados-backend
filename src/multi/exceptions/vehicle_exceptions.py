from . import Error


class VehicleException:
  def notCreated():
    Error("There was a problem creating the vehicle. Please contact the administrator")