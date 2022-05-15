# telecom-user-analytics

![telecom](https://call4free.co.uk/wp-content/uploads/2020/04/Backgrond-of-About-Us.jpg)

This project will answer the questions:

* Is the telecommunications firm worth investing in/ or buying?
* Is there potential for the company to expand?

# Screenshots

![topapps](data/top10apps.png)
![bestManufacturers](data/3_best_handset_manufacturers.png)
![topphones](data/5%20best%20phones%20used%20in%20communication.png)
![corellation](data/corellation.png)
![telecom](data/satisfaction.png)

# Setup
## Docker

You can quickly install it using docker:

```bash
docker pull abelblue/telecom_image:1.0
docker run abelblue/telecom_image:1.0
```

## Installation for linux

```bash
git clone https://github.com/Abel-Blue/telecom-user-analytics.git
cd telecom-user-analytics
sudo python3 setup.py install
```