# Parking Lot System

## Problem Introduction

The Parking Lot System is designed to manage parking spaces for different types of vehicles. Initially, the parking lot is treated as a large ground with predefined slots for each vehicle type. The system dynamically adjusts the number of available slots based on vehicle entry and exit. In the extended version, the parking lot will support multiple floors, each with specific capacities for different vehicle types. Additional features include tracking vehicles by their number, recording entry and exit times, optimized parking allocation, and dynamic parking fee calculation.

## Constraints

1. **Vehicle Types**: The system must support multiple vehicle types (e.g., cars, bikes, trucks), each with an initial slot allocation.
2. **Dynamic Slot Management**: Slots should increase or decrease based on vehicle entry and exit.
3. **Single Ground Parking**: Initially, the parking lot is a single ground with a fixed capacity for each vehicle type.
4. **Dynamic Fee Calculation**: Parking fees should be calculated dynamically based on configurable parameters (e.g., time, vehicle type).
5. **Optimized Allocation**: The system should aim for efficient allocation of parking spaces.

## Extensible Ideas

1. **Multi-Floor Parking**: Introduce multiple floors, each with specific capacities for different vehicle types.
2. **Vehicle Tracking**: Add a service to locate a specific vehicle using its registration number.
3. **Time Tracking**: Record entry and exit times for each vehicle to calculate parking duration.
4. **Optimized Parking**: Implement algorithms to optimize parking space allocation.
5. **Advanced Fee Calculation**: Support complex fee structures based on factors like peak hours, vehicle size, or duration.

## Project Prerequisites

1. **Programming Language**: Choose a language like Java, Python, or Node.js for implementation.
2. **Database**: Use a database (e.g., MySQL, PostgreSQL, or MongoDB) to store vehicle and parking data.
3. **Frameworks**: Use a web framework (e.g., Spring Boot, Flask, or Express.js) for building APIs.
4. **Testing**: Include unit and integration tests to ensure system reliability.
5. **Version Control**: Use Git for version control and collaboration.
### Language Requirement

The project will be implemented using **Python**. No specific libraries are mandatory, but the following are recommended for efficient development:

- **Flask** or **FastAPI**: For building RESTful APIs.
- **SQLAlchemy** or **Django ORM**: For database interaction.
- **pytest**: For unit and integration testing.
- **pandas**: For data manipulation, if needed.
- **datetime**: For handling time-related operations.