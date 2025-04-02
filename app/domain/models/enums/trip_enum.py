from enum import Enum


class TripStatusEnum(Enum):
    PENDING = "pending"      # Passenger requested to join
    CONFIRMED = "confirmed"  # Driver confirmed passenger
    COMPLETED = "completed"  # Trip completed
    CANCELED = "canceled"    # Passenger or driver canceled
