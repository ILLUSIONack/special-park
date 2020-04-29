#### Special Park Technical Component - License Plate Scanner

---

# Explanation

We want visitors to gain access to a parking garage with only their license plate. This component, a [Raspberry Pi 4](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/) will be stationed at the ports of a parking garage. This component will have the job to scan license plates from incoming cars and send validation requests to the server (REST API). The server will respond with a *status*: true or false. True for a succesful validation and false for a does not exist error or account is incomplete.

This module represents the software which the Raspberry Pi 4 will run in order to scan license plates, make validation requests and give visitors access to the parking garage.