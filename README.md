# ALX-portfolio-project_Trade-Share
![Stock Trade](https://user-images.githubusercontent.com/106780350/230334955-c9d8baf9-9bf9-4886-b24d-e7285923a45d.png)

# Description
Trade Share is online investment platform which aims to bring the financial investment from firms to everyone. It provides a plateform for companies to buy and sell shares to the Investres.
The project run on flask framework on port 5000.
Starting the project
 1.Open the api folder
 2. Run the file run.py 
 3. Open your web browser and access the your local host address with port 5000

# Architecture
![ST Achetecture](https://user-images.githubusercontent.com/106780350/230335006-b8b47c38-dd52-433f-b72c-a1c98b64fa43.png)


# Technologies
FRONTEND
* BOOTSTRAP
* HTML
* CSS
* JQUERY

FRONTEND
* FLASK
* MYSQL(sqlAlchemy)
* GUNNICORN
* NGINX

# Data Model
nvestor:  It holds investor details (balance, id , email, name etc)
VIP : use to hold stocks details( price, daily_profie, id)
Deposit_pending : use to hold pending_deposites details( date, number, transaction id, amount)
Deposits: Table that holds all approved deposits
Withdrawal_pending : Table that holds pending withdrawal
Withdrawal : Table that holds all approved withdrawal
Withdrawal_info : It holds withdrawal information of an investor

# Authors
Kingsley Botchway <dondecency11@gmail.com>
Saheed Salawu <saheedsalawu121@gmail.com>
