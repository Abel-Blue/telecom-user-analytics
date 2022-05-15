# telecom-user-analytics

![telecom](https://call4free.co.uk/wp-content/uploads/2020/04/Backgrond-of-About-Us.jpg)

This project will answer the questions:

* Is the telecommunications firm worth investing in/ or buying?
* Is there potential for the company to expand?

# Screenshots
### The top three apps utilized by this telecom company's customers
![topapps](data/top10apps.png)
### The top five phones used by this telecom company's customers
![topphones](data/5%20best%20phones%20used%20in%20communication.png)
### Data transfer coordination between several apps
![corellation](data/corellation.png)

# Setup
## Docker

You can run the dashboard using docker:

```bash
docker pull abelblue/tele_image:1.0
docker run abelblue/tele_image:1.0
```

## Installation for linux

```bash
git clone https://github.com/Abel-Blue/telecom-user-analytics.git
cd telecom-user-analytics
sudo python3 setup.py install
```
## Data visualization link
[visualization link](https://share.streamlit.io/abel-blue/telecom-user-analytics/main/app.py)