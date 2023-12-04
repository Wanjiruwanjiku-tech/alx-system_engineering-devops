LOAD BALANCING
------------------------------------------------

- A load balancer is a crucial component in distributed computing and web hosting environments.

- Its primary function is to distribute incoming network traffic across multiple servers to ensure no single server is overwhelmed with too much load.

- This not only enhances the reliability and availability of the system but also helps in optimizing resource utilization. Here are the key aspects of a load balancer:


1. Load Distribution:
-----------------------------------------------

Algorithm: Load balancers use various algorithms to distribute incoming requests among a pool of servers. Common algorithms include Round Robin, Least Connections, IP Hash, and more.

2. High Availability:
--------------------------------------------

Load balancers enhance the availability of a system by ensuring that if one server fails or becomes unreachable, the remaining servers continue to handle traffic. This is achieved through health checks and automatic re-routing of traffic.

3. Scalability:
--------------------------------------------------------

Load balancers support horizontal scalability by enabling the addition or removal of servers dynamically. As the load increases, new servers can be added to the pool, and as it decreases, servers can be removed.

4. SSL Termination:
---------------------------------------------

Load balancers can offload SSL/TLS encryption and decryption, reducing the computational load on the backend servers. This is known as SSL termination.

5. Session Persistence:
-----------------------------------------------------

Some applications require maintaining a user's session on a specific server. Load balancers can be configured to support session persistence or "sticky sessions," where a user's requests are consistently directed to the same server.

6. Health Checks:
---------------------------------------------

Load balancers regularly check the health of backend servers. If a server fails a health check, the load balancer stops sending traffic to that server until it recovers


- Overall, load balancers play a crucial role in ensuring the scalability, availability, and performance of web applications and services.