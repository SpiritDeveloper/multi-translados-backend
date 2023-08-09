from . import Error


class VehicleException:
  def notFound():
    Error("the vehicle was not found or is disabled")

  def notCreated():
    Error("There was a problem creating the vehicle. Please contact the administrator")