# Roles of client and server in web communication

**1. Role of Client**
-----------------------------------------------------------------------------------------------------
>. a clint is a device or software that request services or resources from a server

1. Sends request to the server (using http/https)
2. display web pages to the user
3. collects user input--forms,loging details
4. processes some data locally like javascript

***Example***

1. web browsers like google chrome
2. firefox
3. microsoft

>. whene you type a websites address the browser sends a request to the server

------------------------------------------------------------------------------------------------------

**Role Of Server**
------------------------------------------------------------------------------------------------------
>. a server is a computers or software that provides services or resources to clint.

1. recives clint request
2. processes the request
3. accesses database if needed
4. sends respones back to client

***Example***
>. when you open a websites the server sends the webpage data back to your browser

-------------------------------------------------------------------------------------------------------
# Network Layers on client and server

1. Application Layer
> used by web browsers and web servers
> protocol-----http/https
> they handels web communications

2. Transport Layers
> protocol---TCP
> they ensures reliable data transfer

3. Network Layer
> protocol---ip
> they Handles addressing and routing of data

4. data link
> transfer data within the local network

5. Physical layer
> sends actual signals cabels or WIfi

# Client-Server Communication Flow

1. client sends http requests 
2. data travels through network layers
3. server receves and processes requests
4. server sends http responses
5. client displays webpage