Postmortem: Service Outage on User Authentication System
Issue Summary
On August 20, 2024, from 14:00 UTC to 16:30 UTC, our User Authentication System experienced a significant outage lasting 2 hours and 30 minutes. During this period, approximately 75% of our users were unable to log in or authenticate their accounts, leading to widespread frustration and disruption in service access. The root cause of the outage was identified as a failure in our database connection pool, which became saturated due to an unexpected surge in user login requests.

Timeline
14:00 UTC - The issue was detected when monitoring alerts indicated a sharp increase in response times for the authentication service.
14:05 UTC - An engineer noticed the alerts and began investigating the authentication service's performance metrics.
14:15 UTC - Initial assumptions pointed to a potential issue with the load balancer, leading to an investigation of load distribution across servers.
14:30 UTC - Customer complaints began flooding in through our support channels, confirming widespread issues with logging in.
14:45 UTC - The incident was escalated to the Site Reliability Engineering (SRE) team for deeper investigation.
15:00 UTC - The SRE team discovered that the database connection pool was exhausted, preventing new connections from being established.
15:15 UTC - A temporary fix was implemented by increasing the maximum number of connections allowed in the pool.
16:30 UTC - The service was fully restored, and normal operations resumed.
Root Cause and Resolution
The outage was caused by the database connection pool reaching its maximum capacity due to an unexpected spike in user authentication requests. This spike was attributed to a marketing campaign that drove a significant increase in user logins. The pool was configured to handle a specific number of concurrent connections, which was insufficient for the sudden load.

To resolve the issue, we first increased the maximum number of concurrent connections in the database connection pool, allowing more users to authenticate simultaneously. Additionally, we implemented a temporary rate-limiting strategy to manage the influx of login requests and prevent overwhelming the system.

Corrective and Preventative Measures
To improve the resilience of our User Authentication System and prevent similar outages in the future, we identified several key areas for enhancement:

Increase Database Connection Pool Size: Adjust the connection pool settings to accommodate higher traffic volumes, especially during marketing campaigns or peak usage times.
Implement Rate Limiting: Develop and deploy a rate-limiting mechanism to manage excessive login requests and protect the authentication service from sudden spikes.
Enhance Monitoring: Improve monitoring on the database connection pool metrics to provide early warnings of saturation and enable proactive scaling.
Load Testing: Conduct regular load testing to simulate high traffic scenarios and ensure the system can handle unexpected surges effectively.
TODO List
 Increase the database connection pool size in the configuration settings.
 Develop a rate-limiting feature for the authentication service.
 Set up alerts for connection pool saturation and response time thresholds.
 Schedule and execute load testing sessions to validate system performance under stress.
 Review and update documentation for incident response protocols related to authentication issues.
By addressing these areas, we aim to enhance the stability and reliability of our User Authentication System, ensuring a better experience for our users and minimizing the risk of future outages.
