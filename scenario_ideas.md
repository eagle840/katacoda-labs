## A list of scenarios for new scenarios/courses to create.

Courses: **CNI**
  1. Basic CNI overview with weave-net
  2. Calico setup (IN PROGRESS)
  3. Flannel setup
  4. troubleshooting cni (see: Troubleshooting On-Premise Kubernetes Network: Underlay, Overlay and Pod - Tomofumi Hayashi, RedHat)

Course: **databases:**
  1. sql
  2. KV - redis
  3. Document: Mongo
  4. Columnar: cassasdra
  5. Graph: Neo4j
  6. DB storage/backup
  *  for each of the db systems, you'll need a cli, ui, (windows app?) and a code test to access db
  
Scenario: **your first custom controller**
  * Use https://www.youtube.com/watch?v=_BuqPMlXfpE   to create this scenario
  
 Scenario: **RabbitMQ**
 
 Scenario: **Use with M$ IOT Demo hub**

Course: **Linux cmds**
   1. tcpdump and netcat (in progress)
   
Course **Authenication systems**
   1. LDAP     use?  https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-a-basic-ldap-server-on-an-ubuntu-12-04-vps        need: ubuntu, port 80 open
      vs 386-ds   from redhat?
   2. Dogtag PKI (and with vault)
      - vault has a playground
      - vault option for pki: https://learn.hashicorp.com/vault/secrets-management/sm-pki-engine
      - docker image for dogtagpki
      - you can use vault with a pki
      - installing dogtag (quickstar)[https://www.dogtagpki.org/wiki/Quick_Start]
         - install ds 1st (html is messed up)
         - then install  dogtag
      - uses 386-ds   (see from 2014)[https://www.youtube.com/watch?v=2qkhm7B01iA]
Scenario: **APIs and webhooks**
   intro: over view of using api's and webhooks
   step1:  curl, gwet, browser, postman other tools
   step2:   api's   - starwars and other database. 
   step3:  webhooks  - webhook test websites
   step4:  trigger a github webhook
   step5:  ???M$devops
   finish:  other resources 
   
Scenario: K8S rbac service accounts
   from: Kubernetes Auth and Access Control by Eric Chiang, CoreOS

Scenario: k8s certs
   from: Certifik8s: All You Need to Know About Certificates in Kubernetes [I] - Alexander Brand, Apprenda

Scenario: etcd HA
   github.com/etcd-io/etcd/tree/master/Documentation