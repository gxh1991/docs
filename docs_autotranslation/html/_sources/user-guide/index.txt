=======================
OpenDaylight User Guide
=======================

:Author: OpenDaylight Community documentation@opendaylight.org
:Date:   2014-07-16

This first part of the user guide covers the basic user operations of
the OpenDaylight Release using the generic base functionality.

OpenDaylight Controller Overview
================================

The OpenDaylight controller is JVM software and can be run from any
operating system and hardware as long as it supports Java. The
controller is an implementation of the Software Defined Network (SDN)
concept and makes use of the following tools:

-  **Maven**: OpenDaylight uses Maven for easier build automation. Maven
   uses pom.xml (Project Object Model) to script the dependencies
   between bundle and also to describe what bundles to load and start.

-  **OSGi**: This framework is the back-end of OpenDaylight as it allows
   dynamically loading bundles and packages JAR files, and binding
   bundles together for exchanging information.

-  **JAVA interfaces**: Java interfaces are used for event listening,
   specifications, and forming patterns. This is the main way in which
   specific bundles implement call-back functions for events and also to
   indicate awareness of specific state.

-  **REST APIs**: These are northbound APIs such as topology manager,
   host tracker, flow programmer, static routing, and so on.

The controller exposes open northbound APIs which are used by
applications. The OSGi framework and bidirectional REST are supported
for the northbound APIs. The OSGi framework is used for applications
that run in the same address space as the controller while the REST
(web-based) API is used for applications that do not run in the same
address space (or even the same system) as the controller. The business
logic and algorithms reside in the applications. These applications use
the controller to gather network intelligence, run its algorithm to do
analytics, and then orchestrate the new rules throughout the network. On
the southbound, multiple protocols are supported as plugins, e.g.
OpenFlow 1.0, OpenFlow 1.3, BGP-LS, and so on. The OpenDaylight
controller starts with an OpenFlow 1.0 southbound plugin. Other
OpenDaylight contributors begin adding to the controller code. These
modules are linked dynamically into a **Service Abstraction Layer**
(SAL).

The SAL exposes services to which the modules north of it are written.
The SAL figures out how to fulfill the requested service irrespective of
the underlying protocol used between the controller and the network
devices. This provides investment protection to the applications as
OpenFlow and other protocols evolve over time. For the controller to
control devices in its domain, it needs to know about the devices, their
capabilities, reachability, and so on. This information is stored and
managed by the **Topology Manager**. The other components like ARP
handler, Host Tracker, Device Manager, and Switch Manager help in
generating the topology database for the Topology Manager.

For a more detailed overview of the OpenDaylight controller, see the
*OpenDaylight Developer Guide*.

Using the OpenDaylight User Interface (DLUX)
============================================

This section introduces you to the OpenDaylight User Experience (DLUX)
application.

Getting Started with DLUX
-------------------------

DLUX provides a number of different Karaf features, which you can enable
and disable separately. In Beryllum they are: . odl-dlux-core .
odl-dlux-node . odl-dlux-yangui . odl-dlux-yangvisualizer

Logging In
----------

To log in to DLUX, after installing the application:

1. Open a browser and enter the login URL
   `http://<your-karaf-ip>:8181/index.html <http://<your-karaf-ip>:8181/index.html>`__
   in your browser (Chrome is recommended).

2. Login to the application with your username and password credentials.

    **Note**

    OpenDaylight’s default credentials are *admin* for both the username
    and password.

Working with DLUX
-----------------

After you login to DLUX, if you enable only odl-dlux-core feature, you
will see only topology application available in the left pane.

    **Note**

    To make sure topology displays all the details, enable the
    odl-l2switch-switch feature in Karaf.

DLUX has other applications such as node, yang UI and those apps won’t
show up, until you enable their features odl-dlux-node and
odl-dlux-yangui respectively in the Karaf distribution.

.. figure:: ./images/dlux-login.png
   :alt: DLUX Modules

   DLUX Modules

    **Note**

    If you install your application in dlux, they will also show up on
    the left hand navigation after browser page refresh.

Viewing Network Statistics
--------------------------

The **Nodes** module on the left pane enables you to view the network
statistics and port information for the switches in the network.

To use the **Nodes** module:

1. Select **Nodes** on the left pane. The right pane displays atable
   that lists all the nodes, node connectors and the statistics.

2. Enter a node ID in the **Search Nodes** tab to search by node
   connectors.

3. Click on the **Node Connector** number to view details such as port
   ID, port name, number of ports per switch, MAC Address, and so on.

4. Click **Flows** in the Statistics column to view Flow Table
   Statistics for the particular node like table ID, packet match,
   active flows and so on.

5. Click **Node Connectors** to view Node Connector Statistics for the
   particular node ID.

Viewing Network Topology
------------------------

The Topology tab displays a graphical representation of network topology
created.

    **Note**

    DLUX does not allow for editing or adding topology information. The
    topology is generated and edited in other modules, e.g., the
    OpenFlow plugin. OpenDaylight stores this information in the MD-SAL
    datastore where DLUX can read and display it.

To view network topology:

1. Select **Topology** on the left pane. You will view the graphical
   representation on the right pane. In the diagram blue boxes represent
   the switches, the black represents the hosts available, and lines
   represents how the switches and hosts are connected.

2. Hover your mouse on hosts, links, or switches to view source and
   destination ports.

3. Zoom in and zoom out using mouse scroll to verify topology for larger
   topologies.

.. figure:: ./images/dlux-topology.png
   :alt: Topology Module

   Topology Module

Interacting with the YANG-based MD-SAL datastore
------------------------------------------------

The **Yang UI** module enables you to interact with the YANG-based
MD-SAL datastore. For more information about YANG and how it interacts
with the MD-SAL datastore, see the *Controller* and *YANG Tools* section
of the *OpenDaylight Developer Guide*.

.. figure:: ./images/dlux-yang-ui-screen.png
   :alt: Yang UI

   Yang UI

To use Yang UI:

1. Select **Yang UI** on the left pane. The right pane is divided in two
   parts.

2. The top part displays a tree of APIs, subAPIs, and buttons to call
   possible functions (GET, POST, PUT, and DELETE).

       **Note**

       Not every subAPI can call every function. For example, subAPIs in
       the *operational* store have GET functionality only.

   Inputs can be filled from OpenDaylight when existing data from
   OpenDaylight is displayed or can be filled by user on the page and
   sent to OpenDaylight.

   Buttons under the API tree are variable. It depends on subAPI
   specifications. Common buttons are:

   -  GET to get data from OpenDaylight,

   -  PUT and POST for sending data to OpenDaylight for saving

   -  DELETE for sending data to OpenDaylight for deleting.

      You must specify the xpath for all these operations. This path is
      displayed in the same row before buttons and it may include text
      inputs for specific path element identifiers.

      .. figure:: ./images/dlux-yang-api-specification.png
         :alt: Yang API Specification

         Yang API Specification

3. The bottom part of the right pane displays inputs according to the
   chosen subAPI.

   -  Lists are handled as a special case. For example, a device can
      store multiple flows. In this case "flow" is name of the list and
      every list element is identified by a unique key value. Elements
      of a list can, in turn, contain other lists.

   -  In Yang UI, each list element is rendered with the name of the
      list it belongs to, its key, its value, and a button for removing
      it from the list.

      .. figure:: ./images/dlux-yang-sub-api-screen.png
         :alt: Yang UI API Specification

         Yang UI API Specification

4. After filling in the relevant inputs, click the **Show Preview**
   button under the API tree to display request that will be sent to
   OpenDaylight. A pane is displayed on the right side with text of
   request when some input is filled.

Displaying Topology on the **Yang UI**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To display topology:

1. Select subAPI network-topology <topology revision number> == >
   operational == > network-topology.

2. Get data from OpenDaylight by clicking on the "GET" button.

3. Click **Display Topology**.

.. figure:: ./images/dlux-yang-topology.png
   :alt: DLUX Yang Topology

   DLUX Yang Topology

Configuring List Elements on the **Yang UI**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lists in Yang UI are displayed as trees. To expand or collapse a list,
click the arrow before name of the list. To configure list elements in
Yang UI:

1. To add a new list element with empty inputs use the plus icon-button
   **+** that is provided after list name.

2. To remove several list elements, use the **X** button that is
   provided after every list element.

   .. figure:: ./images/dlux-yang-list-elements.png
      :alt: DLUX List Elements

      DLUX List Elements

3. In the YANG-based data store all elements of a list must have a
   unique key. If you try to assign two or more elements the same key, a
   warning icon **!** is displayed near their name buttons.

   .. figure:: ./images/dlux-yang-list-warning.png
      :alt: DLUX List Warnings

      DLUX List Warnings

4. When the list contains at least one list element, after the **+**
   icon, there are buttons to select each individual list element. You
   can choose one of them by clicking on it. In addition, to the right
   of the list name, there is a button which will display a vertically
   scrollable pane with all the list elements.

   .. figure:: ./images/dlux-yang-list-button1.png
      :alt: DLUX List Button1

      DLUX List Button1

Running XSQL Console Commands and Queries
=========================================

XSQL Overview
-------------

XSQL is an XML-based query language that describes simple stored
procedures which parse XML data, query or update database tables, and
compose XML output. XSQL allows you to query tree models like a
sequential database. For example, you could run a query that lists all
of the ports configured on a particular module and their attributes.

The following sections cover the XSQL installation process, supported
XSQL commands, and the way to structure queries.

Installing XSQL
---------------

To run commands from the XSQL console, you must first install XSQL on
your system:

1. Navigate to the directory in which you unzipped OpenDaylight

2. Start Karaf:

   ::

       ./bin/karaf

3. Install XSQL:

   ::

       feature:install odl-mdsal-xsql

XSQL Console Commands
---------------------

To enter a command in the XSQL console, structure the command as
follows: **odl:xsql** *<XSQL command>*

The following table describes the commands supported in this
OpenDaylight release.

+-----------------------+----------------------------------------------------+
| **Command**           | **Description**                                    |
+-----------------------+----------------------------------------------------+
| **r**                 | Repeats the last command you executed.             |
+-----------------------+----------------------------------------------------+
| **list vtables**      | Lists the schema node containers that are          |
|                       | currently installed. Whenever an OpenDaylight      |
|                       | module is installed, its YANG model is placed in   |
|                       | the schema context. At that point, the XSQL        |
|                       | receives a notification, confirms that the         |
|                       | module’s YANG model resides in the schema context  |
|                       | and then maps the model to XSQL by setting up the  |
|                       | necessary vtables and vfields. This command is     |
|                       | useful when you need to determine vtable           |
|                       | information for a query.                           |
+-----------------------+----------------------------------------------------+
| **list vfields**      | Lists the vfields present in a specific vtable.    |
| *<vtable name>*       | This command is useful when you need to determine  |
|                       | vfields information for a query.                   |
+-----------------------+----------------------------------------------------+
| **jdbc** *<ip         | When the ODL server is behind a firewall, and the  |
| address>*             | JDBC client cannot connect to the JDBC server, run |
|                       | this command to start the client as a server and   |
|                       | establish a connection.                            |
+-----------------------+----------------------------------------------------+
| **exit**              | Closes the console.                                |
+-----------------------+----------------------------------------------------+
| **tocsv**             | Enables or disables the forwarding of query output |
|                       | as a .csv file.                                    |
+-----------------------+----------------------------------------------------+
| **filename**          | Specifies the .tocsv file to which the query data  |
| *<filename>*          | is exported. If you do not specify a value for     |
|                       | this option when the toccsv option is enabled, the |
|                       | filename for the query data file is generated      |
|                       | automatically.                                     |
+-----------------------+----------------------------------------------------+

Table: Supported XSQL Console Commands

XSQL Queries
------------

You can run a query to extract information that meets the criteria you
specify using the information provided by the **list vtables** and
**list vfields** *<vtable name>* commands. Any query you run should be
structured as follows:

**select** *<vfields you want to search for, separated by a comma and a
space>* **from** *<vtables you want to search in, separated by a comma
and a space>* **where** *<criteria>* ***\*\ *<criteria operator>****;\*

For example, if you want to search the nodes/node ID field in the
nodes/node-connector table and find every instance of the
Hardware-Address object that contains *BA* in its text string, enter the
following query:

::

    select nodes/node.ID from nodes/node-connector where Hardware-Address like '%BA%';

The following criteria operators are supported:

+----------------+-----------------------------------------------------------+
| **Criteria     | **Description**                                           |
| Operators**    |                                                           |
+----------------+-----------------------------------------------------------+
| **=**          | Lists results that equal the value you specify.           |
+----------------+-----------------------------------------------------------+
| **!=**         | Lists results that do not equal the value you specify.    |
+----------------+-----------------------------------------------------------+
| **like**       | Lists results that contain the substring you specify. For |
|                | example, if you specify **like %BC%**, every string that  |
|                | contains that particular substring is displayed.          |
+----------------+-----------------------------------------------------------+
| **<**          | Lists results that are less than the value you specify.   |
+----------------+-----------------------------------------------------------+
| **>**          | Lists results that are more than the value you specify.   |
+----------------+-----------------------------------------------------------+
| **and**        | Lists results that match both values you specify.         |
+----------------+-----------------------------------------------------------+
| **or**         | Lists results that match either of the two values you     |
|                | specify.                                                  |
+----------------+-----------------------------------------------------------+
| **>=**         | Lists results that are more than or equal to the value    |
|                | you specify.                                              |
+----------------+-----------------------------------------------------------+
| **⇐**          | Lists results that are less than or equal to the value    |
|                | you specify.                                              |
+----------------+-----------------------------------------------------------+
| **is null**    | Lists results for which no value is assigned.             |
+----------------+-----------------------------------------------------------+
| **not null**   | Lists results for which any value is assigned.            |
+----------------+-----------------------------------------------------------+
| **skip**       | Use this operator to list matching results from a child   |
|                | node, even if its parent node does not meet the specified |
|                | criteria. See the following example for more information. |
+----------------+-----------------------------------------------------------+

Table: Supported XSQL Query Criteria Operators

Example: Skip Criteria Operator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are looking at the following structure and want to determine all
of the ports that belong to a YY type module:

-  Network Element 1

   -  Module 1, Type XX

      -  Module 1.1, Type YY

         -  Port 1

         -  Port 2

   -  Module 2, Type YY

      -  Port 1

      -  Port 2

If you specify **Module.Type=\ *YY*** in your query criteria, the ports
associated with module 1.1 will not be returned since its parent module
is type XX. Instead, enter **Module.Type=\ *YY* or skip
Module!=\ *YY***. This tells XSQL to disregard any parent module data
that does not meet the type YY criteria and collect results for any
matching child modules. In this example, you are instructing the query
to skip module 1 and collect the relevant data from module 1.1.

Setting Up Clustering
=====================

Clustering Overview
-------------------

Clustering is a mechanism that enables multiple processes and programs
to work together as one entity. For example, when you search for
something on google.com, it may seem like your search request is
processed by only one web server. In reality, your search request is
processed by may web servers connected in a cluster. Similarly, you can
have multiple instances of OpenDaylight working together as one entity.

Advantages of clustering are:

-  Scaling: If you have multiple instances of OpenDaylight running, you
   can potentially do more work and store more data than you could with
   only one instance. You can also break up your data into smaller
   chunks (shards) and either distribute that data across the cluster or
   perform certain operations on certain members of the cluster.

-  High Availability: If you have multiple instances of OpenDaylight
   running and one of them crashes, you will still have the other
   instances working and available.

-  Data Persistence: You will not lose any data stored in OpenDaylight
   after a manual restart or a crash.

The following sections describe how to set up clustering on both
individual and multiple OpenDaylight instances.

Single Node Clustering
----------------------

To enable clustering on a single instance of OpenDaylight, perform the
following steps:

1. Download, unzip, and run the OpenDaylight distribution

2. Install the clustering feature:

   ::

       feature:install odl-mdsal-clustering

    **Note**

    This will enabled the cluster-ready version of the MD-SAL data
    store, but will not actually create a cluster of multiple instances.
    The result is that you will get data persistence, but not the
    scaling or high availability advantages.

Multiple Node Clustering
------------------------

The following sections describe how to set up multiple node clusters in
OpenDaylight.

Deployment Considerations
~~~~~~~~~~~~~~~~~~~~~~~~~

To implement clustering, the deployment considerations are as follows:

-  To set up a cluster with multiple nodes, we recommend that you use a
   minimum of three machines. You can set up a cluster with just two
   nodes. However, if one of the two nodes fail, the cluster will not be
   operational.

       **Note**

       This is because clustering in OpenDaylight requires a majority of
       the nodes to be up and one node cannot be a majority of two
       nodes.

-  Every device that belongs to a cluster needs to have an identifier.
   OpenDaylight uses the node’s ``role`` for this purpose. After you
   define the first node’s role as *member-1* in the ``akka.conf`` file,
   OpenDaylight uses *member-1* to identify that node.

-  Data shards are used to contain all or a certain segment of a
   OpenDaylight’s MD-SAL datastore. For example, one shard can contain
   all the inventory data while another shard contains all of the
   topology data.

   If you do not specify a module in the ``modules.conf`` file and do
   not specify a shard in ``module-shards.conf``, then (by default) all
   the data is placed in the default shard (which must also be defined
   in ``module-shards.conf`` file). Each shard has replicas configured.
   You can specify the details of where the replicas reside in
   ``module-shards.conf`` file.

-  If you have a three node cluster and would like to be able to
   tolerate any single node crashing, a replica of every defined data
   shard must be running on all three cluster nodes.

       **Note**

       This is because OpenDaylight’s clustering implementation requires
       a majority of the defined shard replicas to be running in order
       to function. If you define data shard replicas on two of the
       cluster nodes and one of those nodes goes down, the corresponding
       data shards will not function.

-  If you have a three node cluster and have defined replicas for a data
   shard on each of those nodes, that shard will still function even if
   only two of the cluster nodes are running. Note that if one of those
   remaining two nodes goes down, the shard will not be operational.

-  It is recommended that you have multiple seed nodes configured. After
   a cluster member is started, it sends a message to all of its seed
   nodes. The cluster member then sends a join command to the first seed
   node that responds. If none of its seed nodes reply, the cluster
   member repeats this process until it successfully establishes a
   connection or it is shut down.

-  After a node is unreachable, it remains down for configurable period
   of time (10 seconds, by default). Once a node goes down, you need to
   restart it so that it can rejoin the cluster. Once a restarted node
   joins a cluster, it will synchronize with the lead node
   automatically.

Setting Up a Multiple Node Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To run OpenDaylight in a three node cluster, perform the following:

First, determine the three machines that will make up the cluster. After
that, do the following on each machine:

1. Copy the OpenDaylight distribution zip file to the machine.

2. Unzip the distribution.

3. Open the following .conf files:

   -  configuration/initial/akka.conf

   -  configuration/initial/module-shards.conf

4. In each configuration file, make the following changes:

   a. Find every instance of the following lines and replace *127.0.0.1*
      with the hostname or IP address of the machine on which this file
      resides and OpenDaylight will run:

      ::

          netty.tcp {
            hostname = "127.0.0.1"

          **Note**

          The value you need to specify will be different for each node
          in the cluster.

   b. Find the following lines and replace *127.0.0.1* with the hostname
      or IP address of any of the machines that will be part of the
      cluster:

      ::

          cluster {
            seed-nodes = ["akka.tcp://opendaylight-cluster-data@127.0.0.1:2550"]

   c. Find the following section and specify the role for each member
      node. Here we assign the first node with the *member-1* role, the
      second node with the *member-2* role, and the third node with the
      *member-3* role:

      ::

          roles = [
            "member-1"
          ]

          **Note**

          This step should use a different role on each node.

   d. Open the configuration/initial/module-shards.conf file and update
      the replicas so that each shard is replicated to all three nodes:

      ::

          replicas = [
              "member-1",
              "member-2",
              "member-3"
          ]

      For reference, view a sample config files
      `below <#_sample_config_files>`__.

5. Move into the ``<karaf-distribution-directory>/bin`` directory.

6. Run the following command:

   ::

       JAVA_MAX_MEM=4G JAVA_MAX_PERM_MEM=512m ./karaf

7. Enable clustering by running the following command at the Karaf
   command line:

   ::

       feature:install odl-mdsal-clustering

OpenDaylight should now be running in a three node cluster. You can use
any of the three member nodes to access the data residing in the
datastore.

Sample Config Files
^^^^^^^^^^^^^^^^^^^

**Sample ``akka.conf`` file.**

::

    odl-cluster-data {
      bounded-mailbox {
        mailbox-type = "org.opendaylight.controller.cluster.common.actor.MeteredBoundedMailbox"
        mailbox-capacity = 1000
        mailbox-push-timeout-time = 100ms
      }

      metric-capture-enabled = true

      akka {
        loglevel = "DEBUG"
        loggers = ["akka.event.slf4j.Slf4jLogger"]

        actor {

          provider = "akka.cluster.ClusterActorRefProvider"
          serializers {
                    java = "akka.serialization.JavaSerializer"
                    proto = "akka.remote.serialization.ProtobufSerializer"
                  }

                  serialization-bindings {
                      "com.google.protobuf.Message" = proto

                  }
        }
        remote {
          log-remote-lifecycle-events = off
          netty.tcp {
            hostname = "10.194.189.96"
            port = 2550
            maximum-frame-size = 419430400
            send-buffer-size = 52428800
            receive-buffer-size = 52428800
          }
        }

        cluster {
          seed-nodes = ["akka.tcp://opendaylight-cluster-data@10.194.189.96:2550"]

          auto-down-unreachable-after = 10s

          roles = [
            "member-1"
          ]

        }
      }
    }

    odl-cluster-rpc {
      bounded-mailbox {
        mailbox-type = "org.opendaylight.controller.cluster.common.actor.MeteredBoundedMailbox"
        mailbox-capacity = 1000
        mailbox-push-timeout-time = 100ms
      }

      metric-capture-enabled = true

      akka {
        loglevel = "INFO"
        loggers = ["akka.event.slf4j.Slf4jLogger"]

        actor {
          provider = "akka.cluster.ClusterActorRefProvider"

        }
        remote {
          log-remote-lifecycle-events = off
          netty.tcp {
            hostname = "10.194.189.96"
            port = 2551
          }
        }

        cluster {
          seed-nodes = ["akka.tcp://opendaylight-cluster-rpc@10.194.189.96:2551"]

          auto-down-unreachable-after = 10s
        }
      }
    }

**Sample ``module-shards.conf`` file.**

::

    module-shards = [
        {
            name = "default"
            shards = [
                {
                    name="default"
                    replicas = [
                        "member-1",
                        "member-2",
                        "member-3"
                    ]
                }
            ]
        },
        {
            name = "topology"
            shards = [
                {
                    name="topology"
                    replicas = [
                        "member-1",
                        "member-2",
                        "member-3"
                    ]
                }
            ]
        },
        {
            name = "inventory"
            shards = [
                {
                    name="inventory"
                    replicas = [
                        "member-1",
                        "member-2",
                        "member-3"
                    ]
                }
            ]
        },
        {
             name = "toaster"
             shards = [
                 {
                     name="toaster"
                     replicas = [
                        "member-1",
                        "member-2",
                        "member-3"
                     ]
                 }
             ]
        }
    ]

This second part of the user guide covers project specific usage
instructions.

ALTO User Guide
===============

Overview
--------

The ALTO project provides support for *Application Layer Traffic
Optimization* services defined in `RFC
7285 <https://tools.ietf.org/html/rfc7285>`__.

In the Lithium release, ALTO uses the YANG model described in `this
draft <https://tools.ietf.org/html/draft-shi-alto-yang-model-03>`__.

ALTO Architecture
-----------------

There are three kinds of ALTO packages in OpenDaylight.

1. **Core** The **core** packages include:

   a. ``alto-model``: Defines the YANG model of ALTO services in MD-SAL

   b. ``service-api-rfc7285``: Defines interfaces for ALTO services in
      AD-SAL

   c. ``alto-northbound``: Implements the RFC7285-compatible RESTful API

2. **Basic** The **basic** packages include:

   a. Basic implementations of ALTO services:

      i.  ``alto-provider``: Implements the services defined in
          ``alto-model``

      ii. ``simple-impl``: Implements the services defined in
          ``service-api-rfc7285``

   b. Utilities:

      i. ``alto-manager``: Provides a karaf command line tool to
         manipulate network maps and cost maps.

3. **Service** The **service** packages include:

   a. ``alto-hosttracker``: Generates a network map, a corresponding
      cost map and the endpoint cost service based on
      `l2switch <#_l2switch_user_guide>`__.

Configuring ALTO
----------------

There are three packages that require their own configuration files,
including ``alto-provider``, ``alto-hosttracker`` and ``simple-impl``.
However, the only configurable option is the type of the data broker in
all three configuration files.

Administering or Managing ALTO
------------------------------

To enable ALTO, the features must be installed first.

.. code:: bash

    karaf > feature:install odl-alto-provider
    karaf > feature:install odl-alto-manager
    karaf > feature:install odl-alto-northbound
    karaf > feature:install odl-alto-hosttracker

Managing Data with RESTCONF
~~~~~~~~~~~~~~~~~~~~~~~~~~~

After installing ``odl-alto-provider`` feature in karaf, it is possible
to manage network-maps and cost-maps using RESTCONF. Take a look at all
the operations provided by ``alto-model`` at the API service page which
can be found at ``http://localhost:8181/apidoc/explorer/index.html``.

With the example input below you can insert a network map into the data
store, either by filling the form in the API doc page, or by using tools
such as ``curl``.

.. code:: bash

    HOST_IP=localhost                   # IP address of the controller
    CREDENTIAL=admin:admin              # username and password for authentication
    BASE_URL=$HOST_IP:8181/restconf/config
    SERVICE_PATH=alto-service:resources/alto-service:network-maps/alto-service:network-map
    RESOURCE_ID=test_odl                # Should match the one in the input file
    curl -X PUT -H "content-type:application/yang.data+json" \
                -d @example-input.json -u $CREDENTIAL \
                http://$BASE_URL/$SERVICE_PATH/$RESOURCE_ID

.. code:: json

    {
        "alto-service:network-map": [
            {
                "alto-service:map": [
                    {
                        "alto-service:endpoint-address-group": [
                            {
                                "alto-service:address-type": "ipv4",
                                "alto-service:endpoint-prefix": [
                                    "192.0.2.0/24",
                                    "198.51.100.0/25"
                                ]
                            }
                        ],
                        "alto-service:pid": "PID1"
                    },
                    {
                        "alto-service:endpoint-address-group": [
                            {
                                "alto-service:address-type": "ipv4",
                                "alto-service:endpoint-prefix": [
                                    "198.51.100.128/25"
                                ]
                            }
                        ],
                        "alto-service:pid": "PID2"
                    },
                    {
                        "alto-service:endpoint-address-group": [
                            {
                                "alto-service:address-type": "ipv4",
                                "alto-service:endpoint-prefix": [
                                    "0.0.0.0/0"
                                ]
                            },
                            {
                                "alto-service:address-type": "ipv6",
                                "alto-service:endpoint-prefix": [
                                    "::/0"
                                ]
                            }
                        ],
                        "alto-service:pid": "PID3"
                    }
                ],
                "alto-service:resource-id": "test_odl",
                "alto-service:tag": "da65eca2eb7a10ce8b059740b0b2e3f8eb1d4785"
            }
        ]
    }

Use the following command to see the results:

.. code:: bash

    HOST_IP=localhost                   # IP address of the controller
    CREDENTIAL=admin:admin              # username and password for authentication
    BASE_URL=$HOST_IP:8181/restconf/config
    SERVICE_PATH=alto-service:resources/alto-service:network-maps/alto-service:network-map
    RESOURCE_ID=test_odl
    curl -X GET -u $CREDENTIAL http://$BASE_URL/$SERVICE_PATH/$RESOURCE_ID

Use ``DELETE`` method to remove the data from the data store.

.. code:: bash

    HOST_IP=localhost                   # IP address of the controller
    CREDENTIAL=admin:admin              # username and password for authentication
    BASE_URL=$HOST_IP:8181/restconf/config
    SERVICE_PATH=alto-service:resources/alto-service:network-maps/alto-service:network-map
    RESOURCE_ID=test_odl
    curl -X DELETE -H "content-type:application/yang.data+json" \
                   -u $CREDENTIAL http://$BASE_URL/$SERVICE_PATH/$RESOURCE_ID

Using ``alto-manager``
~~~~~~~~~~~~~~~~~~~~~~

The ``alto-manager`` package provides a karaf command line tool which
wraps up the functions described in the last section.

.. code:: bash

    karaf > alto-create <type> <resource-file>
    karaf > alto-delete <type> <resource-id>

Currently only ``network-map`` and ``cost-map`` are supported. Also the
resource files used in ``alto-manager`` follow the RFC7285-compatible
format instead of RESTCONF format.

The following example shows how to use ``alto-manager`` to put a network
map into the data store.

.. code:: bash

    karaf > alto-create network-map example-rfc7285-networkmap.json

.. code:: json

    {
        "meta" : {
            "resource-id": "test_odl",
            "tag": "da65eca2eb7a10ce8b059740b0b2e3f8eb1d4785"
        },
        "network-map" : {
            "PID1" : {
                "ipv4": [
                    "192.0.2.0/24",
                    "192.51.100.0/25"
                ]
            },
            "PID2": {
                "ipv4": [
                    "192.51.100.128/25"
                ]
            },
            "PID3": {
                "ipv4": [
                    "0.0.0.0/0"
                ],
                "ipv6": [
                    "::/0"
                ]
            }
        }
    }

Using ``alto-hosttracker``
~~~~~~~~~~~~~~~~~~~~~~~~~~

As a real instance of ALTO services, ``alto-hosttracker`` reads data
from ``l2switch`` and generates a network map with resource id
``hosttracker-network-map`` and a cost map with resource id
``hostracker-cost-map``. It can only work with OpenFlow-enabled
networks.

After installing the ``odl-alto-hosttracker`` feature, the corresponding
network map and cost map will be inserted into the data store. Follow
the steps in `how to read data with RESTCONF <#read-restconf>`__ to see
the contents.

Authentication and Authorization Services
=========================================

Authentication Service
----------------------

Authentication uses the credentials presented by a user to identify the
user.

    **Note**

    The Authentication user store provided in the Lithium release does
    not fully support a clustered node deployment. Specifically, the AAA
    user store provided by the H2 database needs to be synchronized
    using out of band means. The AAA Token cache is however
    cluster-capable.

Authentication data model
~~~~~~~~~~~~~~~~~~~~~~~~~

A user requests authentication within a domain in which the user has
defined roles. The user chooses either of the following ways to request
authentication:

-  Provides credentials

-  Creates a token scoped to a domain. In OpenDaylight, a domain is a
   grouping of resources (direct or indirect, physical, logical, or
   virtual) for the purpose of access control.

Terms and definitions in the model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Token
    A claim of access to a group of resources on the controller

Domain
    A group of resources, direct or indirect, physical, logical, or
    virtual, for the purpose of access control

User
    A person who either owns or has access to a resource or group of
    resources on the controller

Role
    Opaque representation of a set of permissions, which is merely a
    unique string as admin or guest

Credential
    Proof of identity such as username and password, OTP, biometrics, or
    others

Client
    A service or application that requires access to the controller

Claim
    A data set of validated assertions regarding a user, e.g. the role,
    domain, name, etc.

Authentication methods
^^^^^^^^^^^^^^^^^^^^^^

| There are three ways a user may authenticate in OpenDaylight:

-  Basic HTTP Authentication

   -  Regular, non-token based, authentication with username/password.

-  Token-based Authentication

   -  Direct authentication: A user presents username/password and a
      domain the user wishes to access to the controller and obtains a
      timed (default is 1 hour) scoped access token. The user then uses
      this token to access RESTCONF (for example).

   -  Federated authentication: A user presents credentials to a
      third-party Identity Provider (for example, SSSD) trusted by the
      controller. Upon successful authentication, the controller returns
      a refresh (unscoped) token with a list of domains that the user
      has access to. The user then presents this refresh token scoped to
      a domain that the user has access to obtain a scoped access token.
      The user then uses this access token to access RESTCONF (for
      example).

Example with token authentication using curl:
'''''''''''''''''''''''''''''''''''''''''''''

(username/password = admin/admin, domain = sdn)

.. code:: bash

    # Create a token
    curl -ik -d 'grant_type=password&username=admin&password=admin&scope=sdn' http://localhost:8181/oauth2/token

    # Use the token (e.g.,  ed3e5e05-b5e7-3865-9f63-eb8ed5c87fb9) obtained from above (default token validity is 1 hour):
    curl -ik -H 'Authorization:Bearer ed3e5e05-b5e7-3865-9f63-eb8ed5c87fb9' http://localhost:8181/restconf/config/toaster:toaster

Example with basic HTTP auth using curl:
''''''''''''''''''''''''''''''''''''''''

.. code:: bash

    curl -ik -u 'admin:admin' http://localhost:8181/restconf/config/toaster:toaster

How the OpenDaylight Authentication Service works
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In direct authentication, a service relationship exists between the user
and the OpenDaylight controller. The user and the controller establish
trust that allows them to use, and validate credentials. The user
establishes user identity through credentials.

In direct authentication, a user request progresses through the
following steps:

1. The user requests the controller administrator for a user account.

       Associated with the user account are user credentials, initially
       created by the administrator. OpenDaylight supports only
       username/password credentials. By default, an administrator
       account is present in OpenDaylight out-of-the-box with the
       default username and password being admin/admin. In addition to
       creating the user account, the controller administrator also
       assigns roles to that account on one or more domain. By default,
       there are two user roles; admin, and user, and there is only one
       domain; sdn.

2. The user presents credentials in a token request to the token service
   within a domain.

3. The request is then passed on to the controller token endpoint.

4. The controller token endpoint uses the credential authentication
   entity which returns a claim for the client.

5. The controller token entity transforms the claim (user, domain, and
   roles) into a token which it then provides to the user.

In federated authentication, with the absence of a direct trust
relationship between the user and the service, a third-party Identity
Provider (IdP) is used for authentication. Federated authentication
relies on third-party identity providers (IdP) to authenticate the user.

The user is authenticated by the trusted IdP and a claim is returned to
the OpenDaylight authentication service. The claim is transformed into
an OpenDaylight claim and successively into a token that is passed on to
the user.

In a federated authentication set-up, the OpenDaylight controller AAA
module provides SSSD claim support. SSSD can be used to map users in an
external LDAP server to users defined on the OpenDaylight controller.

Configuring Authentication service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Changes to AAA configurations can be made as follows:

For Authentication functionality via one of:

-  Webconsole

-  CLI (config command in the Karaf shell)

-  Editing the etc/org.opendaylight.aaa.\*.cfg files directly

For Token Cache Store settings via one of:

-  Editing the 08-authn-config.xml configuration file in
   etc/opendaylight/karaf

-  Using RESTCONF

    **Note**

    Configurations for AAA are all dynamic and require no restart.

Configuring Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^

| To configure features from the Web console:

1. Install the Web console:

   ::

       feature:install webconsole

2. On the console (http://localhost:8181/system/console) (default Karaf
   username/password: karaf/karaf), go to **OSGi** > **Configuration** >
   **OpenDaylight AAA Authentication Configuration**.

   a. **Authorized Clients**: List of software clients that are
      authorized to access OpenDaylight northbound APIs.

   b. **Enable Authentication**: Enable or disable authentication. (The
      default is enable.)

Configuring the token store
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open in a text editor etc/opendaylight/karaf/08-authn-config.xml

       The fields you can configure are as follows:

       a. **timeToLive**: Configure the maximum time, in milliseconds,
          that tokens are to be cached. Default is 360000.

2. Save the file.

    **Note**

    When token’s are expired, they are lazily removed from the cache.

Configuring AAA federation
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. On the console, click **OpenDaylight AAA Federation Configuration**.

2. Use the **Custom HTTP Headers** or **Custom HTTP Attributes** fields
   to specify the HTTP headers or attributes for federated
   authentication. Normally, additional specification beyond the default
   is not required.

    **Note**

    As the changes you make to the configurations are automatically
    committed when they are saved, no restart of the Authentication
    service is required.

Configuring federated authentication
''''''''''''''''''''''''''''''''''''

| Use the following steps to set up federated authentication:

1. Set up an Apache front-end and Apache mods for the OpenDaylight
   controller.

2. Set up mapping rules (from LDAP users to OpenDaylight users).

3. Use the ClaimAuthFilter in federation to allow claim transformation.

Mapping users to roles and domains
''''''''''''''''''''''''''''''''''

| The OpenDaylight authentication service transforms assertions from an
  external federated IdP into Authentication Service data:

1. The Apache web server which fronts OpenDaylight AAA sends data to
   SssdAuthFilter.

2. SssdAuthFilter constructs a JSON document from the data.

3. OpenDaylight Authentication Service uses a general purpose
   transformation mapper to transform the JSON document.

Operational model
'''''''''''''''''

| The mapping model works as follows:

1. Assertions from an IdP are stored in an associative array.

2. A sequence of rules is applied, and the first rule which returns
   success is considered a match.

3. Upon success, an associative array of mapped values is returned.

   -  The mapped values are taken from the local variables set during
      the rule execution.

   -  The definition of the rules and mapped results are expressed in
      JSON notation.

Operational Model: Sample code
''''''''''''''''''''''''''''''

.. code:: java

    mapped = null
    foreach rule in rules {
        result = null
        initialize rule.variables with pre-defined values

        foreach block in rule.statement_blocks {
            for statement in block.statements {
                if statement.verb is exit {
                    result = exit.status
                    break
                }
                elif statement.verb is continue {
                    break
                }
            }
            if result {
                break
            }
        if result == null {
            result = success
        }
    if result == success {
        mapped = rule.mapping(rule.variables)
    }
    return mapped

Mapping Users
'''''''''''''

| A JSON Object acts as a mapping template to produce the final
  associative array of name/value pairs. The value in a name/value pair
  can be a constant or a variable. An example of a mapping template and
  rule variables in JSON:
| Template:

.. code:: json

    {
        "organization": "BigCorp.com",
        "user: "$subject",
        "roles": "$roles"
    }

| Local variables:

.. code:: json

    {
        "subject": "Sally",
        "roles": ["user", "admin"]
    }

| The final mapped result will be:

.. code:: json

    {
        "organization": "BigCorp.com",
        "user: "Sally",
        "roles": ["user", "admin"]
    }

Example: Splitting a fully qualified username into user and realm components
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Some IdPs return a fully qualified username (for example, principal or
subject). The fully qualified username is the concatenation of the user
name, separator, and realm name. The following example shows the mapped
result that returns the user and realm as independent values for the
fully qualified username is bob@example.com .

| The mapping in JSON:

.. code:: json

    {
        "user": "$username",
        "realm": "$domain"
    }

| The assertion in JSON:

.. code:: json

    {
        "Principal": "bob@example.com"
    }

| The rule applied:

.. code:: json

    [
        [
            ["in", "Principal", "assertion"],
            ["exit", "rule_fails", "if_not_success"],
            ["regexp", "$assertion[Principal]", (?P<username>\\w+)@(?P<domain>.+)"],
            ["set", "$username", "$regexp_map[username]"],
            ["set", "$domain", "$regexp_map[domain]"],
            ["exit, "rule_succeeds", "always"]
        ]
    ]

| The mapped result in JSON:

.. code:: json

    {
        "user": "bob",
        "realm": "example.com"
    }

Also, users may be granted roles based on their membership in certain
groups.

The Authentication Service allows white lists for users with specific
roles. The white lists ensure that users are unconditionally accepted
and authorized with specific roles. Users who must be unconditionally
denied access can be placed in a black list.

Administering OpenDaylight Authentication Services
--------------------------------------------------

Actors in the System
~~~~~~~~~~~~~~~~~~~~

| **OpenDaylight Controller administrator**
| The OpenDaylight Controller administrator has the following
  responsibilities:

-  Author Authentication policies using the IdmLight Service API

-  Provides credentials, usernames and passwords to users who request
   them

| **OpenDaylight resource owners**
| Resource owners authenticate (either by means of federation or
  directly providing their own credentials to the controller) to obtain
  an access token. This access token can then be used to access
  resources on the controller. An OpenDaylight resource owner enjoys the
  following privileges:

-  Creates, refreshes, or deletes access tokens

-  Gets access tokens from the Secure Token Service

-  Passes secure tokens to resource users

| **OpenDaylight resource users**
| Resource users do not need to authenticate: they can access resources
  if they are given an access tokens by the resource owner. The default
  timeout for access tokens is 1 hour (This duration is configurable.).
  An OpenDaylight resource user does the following:

-  Gets access tokens either from a resource owner or the controller
   administrator

-  Uses tokens at access applications from the north-bound APIs

System Components
~~~~~~~~~~~~~~~~~

IdmLight Identity manager
    Stores local user authentication and authorization data, provides an
    Admin REST API for CRUD operations.

Pluggable authenticators
    Provides domain-specific authentication mechanisms

Authenticator
    Authenticates users against and establishes claims

Authentication Cache
    Caches all authentication states and tokens

Authentication Filter
    Verifies tokens and extracts claims

Authentication Manager
    Contains the session token and authentication claim store

IdmLight Identity manager
^^^^^^^^^^^^^^^^^^^^^^^^^

The Light-weight Identity Manager (IdmLight) Stores local user
authentication and authorization data, and roles and provides an Admin
REST API for CRUD operations on the users/roles/domains database. The
IdmLight REST API is by default accessed via the {controller
baseURI:8181}/auth/v1/ API end point. Access to the API is restricted to
authenticated clients only, or those possessing a token:

Example: To retrieve the users list.

.. code:: bash

    curl http://admin:admin@localhost:8181/auth/v1/users

The following document contains a detailed list of supported CRUD
operations allowed by the API:

::

    https://wiki.opendaylight.org/images/a/ad/AAA_Idmlight_REST_APIs.xlsx

OpenDaylight Authorization Service
----------------------------------

The authorization service currently included in OpenDaylight is of an
experimental kind and only briefly documented here. Authorization
follows successful authentication and is modeled on the Role Based
Access Control (RBAC) approach for defining permissions and decide
access levels to API resources on the controller.

Armoury
=======

This section describes how to use the Armoury feature in OpenDaylight
and contains contains configuration, administration, and management
sections for the feature.

Overview
--------

Just as compute needs to make requests to the controller to get
networking resources in order to provide its services, so too does the
controller sometimes need to make requests of the workload manager to
get compute resources and/or network function (NF) (physical or virtual)
orchestration to provide its services.

Armoury Architecture
--------------------

There are mainly three components :

-  **Armoury Catalog** A registry or catalog of the necessary
   information (images, metadata, templatized day 0 config, how to
   communicate with the NF, etc) to describe the NF to the workload
   manager and/or network function (NF) (physical or virtual)
   orchestration.

-  **Armoury Workload Manager** The most minimal possible API to allow
   applications to request that the workload manager start/stop/etc the
   NF and some information from the workload manager/nf orchestrator
   about the state of the NF.

-  **Armoury Driver Registry** Example Drivers to talk to various
   workload managers (OpenStack/Meseophere/Docker/ Kubernetes/etc).

Armoury Catalog
---------------

The NF Catalog contains metadata describing a NF.

Configuring Armoury Catalog
~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD: Describe how to configure Armoury Catalog after installation.

Administering Armoury Catalog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD: Include related command reference or operations for using Armoury
Catalog.

Armoury Workload Manager
------------------------

The Workload Manager defines RPCs to manage instances.

Configuring Armoury Workload Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD: Describe how to configure Armoury Workload Manager after
installation.

Administering Armoury Workload Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD: Include related command reference or operations for using Armoury
Workload Manager.

Armoury Driver Registry
-----------------------

The Driver Registry Describes the driver that is used to talk with the
workload manager (OpenStack/Meseophere/Docker/Kubernetes/etc).

Configuring Armoury Driver Registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD: Describe how to configure Armoury Driver Registry.

Administering Armoury Driver Registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD: Include related command reference or operations for using Driver
Registry.

Tutorials
---------

Below are tutorials for Armoury.

Using Armoury Catalog
~~~~~~~~~~~~~~~~~~~~~

TBD: State the purpose of tutorial

Overview
^^^^^^^^

TBD: An overview of the Armoury Catalog tutorial

Prerequisites
^^^^^^^^^^^^^

TBD: Provide any prerequisite information, assumed knowledge, or
environment required to execute the use case.

Target Environment
^^^^^^^^^^^^^^^^^^

TBD: Include any topology requirement for the use case.

Instructions
^^^^^^^^^^^^

TBD: Step by step procedure for using Armoury Catalog.

Using Armoury Workload Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD: State the purpose of tutorial

Overview
^^^^^^^^

TBD: An overview of the Armoury Workload Manager tutorial

Prerequisites
^^^^^^^^^^^^^

TBD: Provide any prerequisite information, assumed knowledge, or
environment required to execute the use case.

Target Environment
^^^^^^^^^^^^^^^^^^

TBD: Include any topology requirement for the use case.

Instructions
^^^^^^^^^^^^

TBD: Step by step procedure for using Armoury Workload Manager.

Using Armoury Driver Registry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD: State the purpose of tutorial

Overview
^^^^^^^^

TBD: An overview of the Armoury Driver Registry tutorial

Prerequisites
^^^^^^^^^^^^^

TBD: Provide any prerequisite information, assumed knowledge, or
environment required to execute the use case.

Target Environment
^^^^^^^^^^^^^^^^^^

TBD: Include any topology requirement for the use case.

Instructions
^^^^^^^^^^^^

TBD: Step by step procedure for using Armoury Driver Registry.

BGP User Guide
==============

Overview
--------

The OpenDaylight Karaf distribution comes pre-configured with baseline
BGP configuration. You can find it in the etc/opendaylight/karaf
directory and it consists of two files:

-  **31-bgp.xml** (defines the basic parser and RIB support)

-  **41-bgp-example.xml** (which contains a sample configuration which
   needs to be customized to your deployment)

The next sections will describe how to configure BGP manually or using
RESTCONF.

Configuring BGP
---------------

RIB
~~~

.. code:: xml

    <module>
        <type>prefix:rib-impl</type>
        <name>example-bgp-rib</name>
        <rib-id>example-bgp-rib</rib-id>
        <local-as>64496</local-as>
        <bgp-id>192.0.2.2</bgp-id>
        <cluster-id>192.0.2.3</cluster-id>
        ...
    </module>

-  **rib-id** - BGP RIB Identifier, in this configuration file you can
   specify more BGP RIBs by copy-pasting the above module. These RIBs
   must have a unique rib-id and name.

-  **local-as** - Our local AS number (where OpenDaylight is deployed),
   we use this in best path selection

-  **bgp-id** - Our local BGP identifier (the IP of the VM where
   OpenDaylight is deployed), we use this in best path selection.

-  **cluster-id** - Cluster Identifier, non-mandatory, if not specified,
   BGP Identifier will be used

MIGHT NOT BE NEEDED: depending on your BGP router, you might need to
switch from linkstate attribute type 99 to 29. Check with your router
vendor. Change the field iana-linkstate-attribute-type to true if your
router supports type 29. This snippet is located in 31-bgp.xml file.

.. code:: xml

    <module>
     <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:linkstate">prefix:bgp-linkstate</type>
     <name>bgp-linkstate</name>
     <iana-linkstate-attribute-type>true</iana-linkstate-attribute-type>
    </module>

-  **iana-linkstate-attribute-type** - IANA has issued an early
   allocation for the BGP Linkstate path attribute (=29). To preserve
   (TYPE = 99) set value bellow to false; to use IANA assigned type set
   the value to true or remove it as it’s true by default.

BGP Peer
~~~~~~~~

The initial configuration is written so that it will be ignored to
prevent the client from starting with default configuration. Therefore
the first step is to uncomment the module containing bgp-peer.

.. code:: xml

    <module>
     <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">prefix:bgp-peer</type>
     <name>example-bgp-peer</name>
     <host>192.0.2.1</host>
     <holdtimer>180</holdtimer>
     <peer-role>ibgp</peer-role>
     <rib>
      <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">prefix:rib-instance</type>
      <name>example-bgp-rib</name>
     </rib>
     ...
    </module>

-  **name** - BGP Peer name, in this configuration file you can specify
   more BGP Peers by copy-pasting the above module. These peers must
   have a **unique** name.

-  **host** - IP address or hostname of BGP speaker (IP where
   OpenDaylight should connect to gather topology)

-  **holdtimer** - unit: seconds

-  **peer-role** - If peer role is not present, default value "ibgp"
   will be used (allowed values are also "ebgp" and "rr-client"). This
   field is case-sensitive.

-  **rib** - BGP RIB identifier

Configure Connection Attributes - OPTIONAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: xml

    <module>
       <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:reconnectstrategy">prefix:timed-reconnect-strategy</type>
       <name>example-reconnect-strategy</name>
       <min-sleep>1000</min-sleep>
       <max-sleep>180000</max-sleep>
       <sleep-factor>2.00</sleep-factor>
       <connect-time>5000</connect-time>
       <executor>
           <type xmlns:netty="urn:opendaylight:params:xml:ns:yang:controller:netty">netty:netty-event-executor</type>
           <name>global-event-executor</name>
       </executor>
    </module>

-  **min-sleep** - Minimum sleep time (miliseconds) in between reconnect
   tries

-  **max-sleep** - Maximum sleep time (miliseconds) in between reconnect
   tries

-  **sleep-factor** - Power factor of the sleep time between reconnect
   tries

-  **connect-time** - How long we should wait (miliseconds) for the TCP
   connect attempt, overrides default connection timeout dictated by TCP
   retransmits

BGP Speaker Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~

Previous entries addressed the configuration of a BGP connection
initiated by OpenDaylight. OpenDaylight also supports BGP Speaker
functionality and accepts incoming BGP connections.

\*The configuration of BGP speaker is located in: 41-bgp-example.xml:

.. code:: xml

    <module>
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">prefix:bgp-peer-acceptor</type>
        <name>bgp-peer-server</name>

        <!--Default parameters-->
        <!--<binding-address>0.0.0.0</binding-address>-->
        <!--<binding-port>1790</binding-port>-->

        ...
        <!--Drops or accepts incoming BGP connection, every BGP Peer that should be accepted needs to be added to this registry-->
        <peer-registry>
            <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">prefix:bgp-peer-registry</type>
            <name>global-bgp-peer-registry</name>
        </peer-registry>
    </module>

**Changing speaker configuration** - Changing binding address: Uncomment
tag binding-address and change the address to e.g. *127.0.0.1*. The
default binding address is *0.0.0.0*. - Changing binding port: Uncomment
tag binding-port and change the port to e.g. *1790*. The default binding
port is *179* as specified in `BGP
RFC <http://tools.ietf.org/html/rfc4271>`__.  — 

Incomming BGP Connections
~~~~~~~~~~~~~~~~~~~~~~~~~

**BGP speaker drops all BGP connections from unknown BGP peers.** The
decision is made in component bgp-peer-registry that is injected into
the speaker (The registry is configured in 31-bgp.xml).

To add BGP Peer configuration into the registry, it is necessary to
configure regular BGP peer just like in example in 41-bgp-example.xml.
Notice that the BGP peer depends on the same bgp-peer-registry as
bgp-speaker:

.. code:: xml

    <module>
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">prefix:bgp-peer</type>
        <name>example-bgp-peer</name>
        <host>192.0.2.1</host>
        ...
        <peer-registry>
            <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">prefix:bgp-peer-registry</type>
            <name>global-bgp-peer-registry</name>
        </peer-registry>
        ...
    </module>

The BGP peer registers itself into the registry, which allows incoming
BGP connections handled by the bgp-speaker. (Config attribute
peer-registry is optional for now to preserve backwards compatibility).
With this configuration, the connection to 192.0.2.1 is initiated by
OpenDaylight but will also be accepted from 192.0.2.1. In case both
connections are being established, only one of them will be preserved
and the other will be dropped. The connection initiated from device with
lower bgp id will be dropped by the registry. Each BGP peer must be
configured in its own module. Note, that the name of the module needs to
be unique, so if you are configuring more peers, when changing the
**host**, change also the **name**. There is a way to configure the peer
only for incoming connections (The connection will not be initiated by
the OpenDaylight, OpenDaylight will only wait for incoming connection
from the peer. The peer is identified by its IP address). To configure
peer only for incoming connection add attribute initiate-connection to
peer’s configuration:

.. code:: xml

    <module>
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">prefix:bgp-peer</type>
        <name>example-bgp-peer</name>
        <host>192.0.2.1</host>                         // IP address or hostname of the speaker
        <holdtimer>180</holdtimer>
        <initiate-connection>false</initiate-connection>  // Connection will not be initiated by ODL
        ...
    </module>

-  **initiate-connection** - if set to false OpenDaylight will not
   initiate connection to this peer. Default value is true for all
   peers.

BGP Application Peer
~~~~~~~~~~~~~~~~~~~~

A BGP speaker needs to register all peers that can be connected to it
(meaning if a BGP peer is not configured, the connection with
OpenDaylight won’t be successful). As a first step, configure RIB. Then,
instead of configuring regular peer, configure this application peer,
with its own application RIB. Change the value in bold bgp-peer-id which
is your local BGP-ID that will be used in BGP Best Path Selection
algorithm.

.. code:: xml

    <module>
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:bgp-application-peer</type>
     <name>example-bgp-peer-app</name>
     <bgp-peer-id>10.25.1.9</bgp-peer-id>
     <target-rib>
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:rib-instance</type>
      <name>example-bgp-rib</name>
     </target-rib>
     <application-rib-id>example-app-rib</application-rib-id>
     ...
    </module>

-  **bgp-peer-id** - Our local BGP identifier (the IP of the VM where
   OpenDaylight is deployed), we use this in best path selection

-  **target-rib** - RIB ID of existing RIB where the data should be
   transferred

-  **application-rib-id** - RIB ID of local application RIB (all the
   routes that you put to OpenDaylight will be displayed here)

Configuration through RESTCONF
------------------------------

Another method to configure BGP is dynamically through RESTCONF. Before
you start, make sure, you’ve completed steps 1-5 in Installation Guide.
Instead of restarting Karaf, install another feature, that provides you
the access to *restconf/config/* URLs.

feature:install odl-netconf-connector-all

To check what modules you have currently configured, check following
link:
http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules/
This URL is also used to POST new configuration. If you want to change
any other configuration that is listed here, make sure you include the
correct namespaces. RESTCONF will tell you if some namespace is wrong.

To update an existing configuration use **PUT** and give the full path
to the element you wish to update.

It is vital that you respect the order of steps described in user guide.

RIB
~~~

First, configure RIB. This module is already present in the
configuration, therefore we change only the parameters we need. In this
case, it’s **bgp-rib-id** and **local-as**.

**URL:** \_
*http://127.0.0.1:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules/module/odl-bgp-rib-impl-cfg:rib-impl/example-bgp-rib*

**PUT:**

.. code:: xml

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:rib-impl</type>
     <name>example-bgp-rib</name>
     <session-reconnect-strategy xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:protocol:framework">x:reconnect-strategy-factory</type>
      <name>example-reconnect-strategy-factory</name>
     </session-reconnect-strategy>
     <rib-id xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">example-bgp-rib</rib-id>
     <extensions xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:spi">x:extensions</type>
      <name>global-rib-extensions</name>
     </extensions>
     <codec-tree-factory xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:md:sal:binding">x:binding-codec-tree-factory</type>
      <name>runtime-mapping-singleton</name>
     </codec-tree-factory>
     <tcp-reconnect-strategy xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:protocol:framework">x:reconnect-strategy-factory</type>
      <name>example-reconnect-strategy-factory</name>
     </tcp-reconnect-strategy>
     <data-provider xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:md:sal:binding">x:binding-async-data-broker</type>
      <name>pingpong-binding-data-broker</name>
     </data-provider>
     <local-as xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">64496</local-as>
     <bgp-dispatcher xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type>bgp-dispatcher</type>
      <name>global-bgp-dispatcher</name>
     </bgp-dispatcher>
     <dom-data-provider xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:md:sal:dom">x:dom-async-data-broker</type>
      <name>pingpong-broker</name>
     </dom-data-provider>
     <local-table xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type>bgp-table-type</type>
      <name>ipv4-unicast</name>
     </local-table>
     <local-table xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type>bgp-table-type</type>
      <name>ipv6-unicast</name>
     </local-table>
     <local-table xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type>bgp-table-type</type>
      <name>linkstate</name>
     </local-table>
     <local-table xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type>bgp-table-type</type>
      <name>flowspec</name>
     </local-table>
     <bgp-rib-id xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">192.0.2.2</bgp-rib-id>
    </module>

    **Important**

    MIGHT NOT BE NEEDED depending on your BGP router, you might need a
    switch from linkstate attribute type 99 to 29. Check with your
    router vendor. Switch the field to true if your router supports type
    29.

**URL:**
*http://127.0.0.1:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules/module/odl-bgp-linkstate-cfg:bgp-linkstate/bgp-linkstate*

**PUT:**

.. code:: xml

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:linkstate">x:bgp-linkstate</type>
     <name>bgp-linkstate</name>
     <iana-linkstate-attribute-type xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:linkstate">true</iana-linkstate-attribute-type>
    </module>

BGP Peer
~~~~~~~~

We also need to add new module to configuration (bgp-peer). In this
case, the whole module needs to be configured. Please change values
**host**, **holdtimer** and **peer-role** (if necessary).

****POST:**.**

.. code:: xml

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:bgp-peer</type>
     <name>example-bgp-peer</name>
     <host xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">192.0.2.1</host>
     <holdtimer xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">180</holdtimer>
     <peer-role xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">ibgp</peer-role>
     <rib xmlns"urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:rib-instance</type>
      <name>example-bgp-rib</name>
     </rib>
     <peer-registry xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:bgp-peer-registry</type>
      <name>global-bgp-peer-registry</name>
     </peer-registry>
     <advertized-table xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:bgp-table-type</type>
      <name>ipv4-unicast</name>
     </advertized-table>
     <advertized-table xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:bgp-table-type</type>
      <name>ipv6-unicast</name>
     </advertized-table>
     <advertized-table xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:bgp-table-type</type>
      <name>linkstate</name>
     </advertized-table>
     <advertized-table xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:bgp-table-type</type>
      <name>flowspec</name>
     </advertized-table>
    </module>

This is all necessary information that you need to get ODL connect to
your speaker.

BGP Application Peer
~~~~~~~~~~~~~~~~~~~~

Change the value **bgp-peer-id** which is your local BGP ID that will be
used in BGP Best Path Selection algorithm.

****POST:**.**

.. code:: xml

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:bgp-application-peer</type>
     <name>example-bgp-peer-app</name>
     <bgp-peer-id xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">10.25.1.9</bgp-peer-id> <!-- Your local BGP-ID that will be used in BGP Best Path Selection algorithm -->
     <target-rib xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:rib-instance</type>
      <name>example-bgp-rib</name>
      </target-rib>
     <application-rib-id xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">example-app-rib</application-rib-id>
     <data-broker xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:md:sal:dom">x:dom-async-data-broker</type>
      <name>pingpong-broker</name>
     </data-broker>
    </module>

Tutorials
---------

Viewing BGP Topology
~~~~~~~~~~~~~~~~~~~~

This section summarizes how data from BGP can be viewed through
RESTCONF. Currently it is the only way to view the data.

    **Important**

    From Helium release the port changed from 8080 to 8181.

Network Topology View
^^^^^^^^^^^^^^^^^^^^^

Basic URL for network topology is
**http://localhost:8181/restconf/operational/network-topology:network-topology/**
.

If BGP is configured properly, it should display output similar to this
one:

.. code:: xml

    <network-topology>
     <topology>
      <topology-id>pcep-topology</topology-id>
      <topology-types>
       <topology-pcep/>
      </topology-types>
     </topology>
     <topology>
      <server-provided>true</server-provided>
      <topology-id>example-ipv4-topology</topology-id>
      <topology-types/>
     </topology>
     <topology>
      <server-provided>true</server-provided>
      <topology-id>example-linkstate-topology</topology-id>
      <topology-types/>
     </topology>
    </network-topology>

BGP data as were sent from BGP speaker are listed in three topologies
(if all three are configured):

**example-linkstate-topology** - displays links and nodes advertised
through linkstate Update messages

http://localhost:8181/restconf/operational/network-topology:network-topology/topology/example-linkstate-topology

**example-ipv4-topology** - display Ipv4 adresses of nodes in the
topology

http://localhost:8181/restconf/operational/network-topology:network-topology/topology/example-ipv4-topology

**example-ipv6-topology** - display Ipv6 adresses of nodes in the
topology

http://localhost:8181/restconf/operational/network-topology:network-topology/topology/example-ipv6-topology

Route Information Base (RIB) View
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another view of BGP data is through **BGP RIBs**, located here:

http://localhost:8181/restconf/operational/bgp-rib:bgp-rib/

There are multiple RIBs configured:

-  AdjRibsIn (per Peer) : Adjacency RIBs In, BGP routes as they come
   from BGP Peer

-  EffectiveRib (per Peer) : BGP routes after applying Import policies

-  LocRib (per RIB) : Local RIB, BGP routes from all peers

-  AdjRibsOut (per Peer) : BGP routes that will be advertizes, after
   applying Export policies

This is how the output looks like, when address families for IPv4 and
Linkstate were configured:

.. code:: xml

    <loc-rib>
     <tables>
      </attributes>
      <safi>x:linkstate-subsequent-address-family</safi>
      <afi>x:linkstate-address-family</afi>
      </linkstate-routes>
     </tables>
     <tables>
      </attributes>
      <safi>x:unicast-subsequent-address-family</safi>
      <afi>x:ipv4-address-family</afi>
      </ipv4-routes>
     </tables>
    </loc-rib>

You can see details for each AFI by expanding the RESTCONF link:

**IPv4** :
http://localhost:8181/restconf/operational/bgp-rib:bgp-rib/rib/example-bgp-rib/loc-rib/tables/bgp-types:ipv4-address-family/bgp-types:unicast-subsequent-address-family/ipv4-routes

**Linkstate** :
http://localhost:8181/restconf/operational/bgp-rib:bgp-rib/rib/example-bgp-rib/loc-rib/tables/bgp-linkstate:linkstate-address-family/bgp-linkstate:linkstate-subsequent-address-family/linkstate-routes

Populate RIB
~~~~~~~~~~~~

If your peer is configured, you can populate the RIB by making following
POST call to RESTCONF:

**URL:**
http://localhost:8181/restconf/config/bgp-rib:application-rib/example-app-rib/tables/bgp-types:ipv4-address-family/bgp-types:unicast-subsequent-address-family/

-  where example-app-rib is your application RIB id (that you specified
   in the configuration) and tables specifies AFI and SAFI of the data
   that you want to add.

**POST:**

**Content-Type:** application/xml

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <ipv4-routes xmlns="urn:opendaylight:params:xml:ns:yang:bgp-inet">
     <ipv4-route>
      <prefix>200.20.160.1/32</prefix>
      <attributes>
       <ipv4-next-hop>
        <global>199.20.160.41</global>
       </ipv4-next-hop><as-path/>
       <multi-exit-disc>
        <med>0</med>
       </multi-exit-disc>
       <local-pref>
        <pref>100</pref>
       </local-pref>
       <originator-id>
        <originator>41.41.41.41</originator>
       </originator-id>
       <origin>
        <value>igp</value>
       </origin>
       <cluster-id>
        <cluster>40.40.40.40</cluster>
       </cluster-id>
      </attributes>
     </ipv4-route>
    </ipv4-routes>

The request results in **204 No content**. This is expected.

CAPWAP User Guide
=================

This document describes how to use the Control And Provisioning of
Wireless Access Points (CAPWAP) feature in OpenDaylight. This document
contains configuration, administration, and management sections for the
feature.

Overview
--------

CAPWAP feature fills the gap OpenDaylight Controller has with respect to
managing CAPWAP compliant wireless termination point (WTP) network
devices present in enterprise networks. Intelligent applications (e.g.
centralized firmware management, radio planning) can be developed by
tapping into the WTP network device’s operational states via REST APIs.

CAPWAP Architecture
-------------------

The CAPWAP feature is implemented as an MD-SAL based provider module,
which helps discover WTP devices and update their states in MD-SAL
operational datastore.

Scope of CAPWAP Project
-----------------------

In the Lithium release, CAPWAP project aims to only detect the WTPs and
store their basic attributes in the operational data store, which is
accessible via REST and JAVA APIs.

Installing CAPWAP
-----------------

To install CAPWAP, download OpenDaylight and use the Karaf console to
install the following feature:

odl-capwap-ac-rest

Configuring CAPWAP
------------------

As of Lithium, there are no configuration requirements.

Administering or Managing CAPWAP
--------------------------------

After installing the odl-capwap-ac-rest feature from the Karaf console,
users can administer and manage CAPWAP from the APIDOCS explorer.

Go to
`http://${ipaddress}:8181/apidoc/explorer/index.html <http://${ipaddress}:8181/apidoc/explorer/index.html>`__,
sign in, and expand the capwap-impl panel. From there, users can execute
various API calls.

Tutorials
---------

Viewing Discovered WTPs
~~~~~~~~~~~~~~~~~~~~~~~

Overview
^^^^^^^^

This tutorial can be used as a walk through to understand the steps for
starting the CAPWAP feature, detecting CAPWAP WTPs, accessing the
operational states of WTPs.

Prerequisites
^^^^^^^^^^^^^

It is assumed that user has access to at least one hardware/software
based CAPWAP compliant WTP. These devices should be configured with
OpenDaylight controller IP address as a CAPWAP Access Controller (AC)
address. It is also assumed that WTPs and OpenDaylight controller share
the same ethernet broadcast domain.

Instructions
^^^^^^^^^^^^

1. Run the OpenDaylight distribution and install odl-capwap-ac-rest from
   the Karaf console.

2. Go to
   `http://${ipaddress}:8181/apidoc/explorer/index.html <http://${ipaddress}:8181/apidoc/explorer/index.html>`__

3. Expand capwap-impl

4. Click /operational/capwap-impl:capwap-ac-root/

5. Click "Try it out"

6. The above step should display list of WTPs discovered using ODL
   CAPWAP feature.

DIDM User Guide
===============

Overview
--------

The Device Identification and Driver Management (DIDM) project addresses
the need to provide device-specific functionality. Device-specific
functionality is code that performs a feature, and the code is
knowledgeable of the capability and limitations of the device. For
example, configuring VLANs and adjusting FlowMods are features, and
there may be different implementations for different device types.
Device-specific functionality is implemented as Device Drivers. Device
Drivers need to be associated with the devices they can be used with. To
determine this association requires the ability to identify the device
type.

DIDM Architecture
-----------------

The DIDM project creates the infrastructure to support the following
functions:

-  **Discovery** - Determination that a device exists in the controller
   management domain and connectivity to the device can be established.
   For devices that support the OpenFlow protocol, the existing
   discovery mechanism in OpenDaylight suffices. Devices that do not
   support OpenFlow will be discovered through manual means such as the
   operator entering device information via GUI or REST API.

-  **Identification** – Determination of the device type.

-  **Driver Registration** – Registration of Device Drivers as routed
   RPCs.

-  **Synchronization** – Collection of device information, device
   configuration, and link (connection) information.

-  **Data Models for Common Features** – Data models will be defined to
   perform common features such as VLAN configuration. For example,
   applications can configure a VLAN by writing the VLAN data to the
   data store as specified by the common data model.

-  **RPCs for Common Features** – Configuring VLANs and adjusting
   FlowMods are example of features. RPCs will be defined that specify
   the APIs for these features. Drivers implement features for specific
   devices and support the APIs defined by the RPCs. There may be
   different Driver implementations for different device types.

Group Based Policy User Guide
=============================

Overview
--------

OpenDaylight Group Based Policy allows users to express network
configuration in a declarative versus imperative way.

This is often described as asking for **"what you want"**, rather than
**"how to do it"**.

In order to achieve this Group Based Policy (herein referred to as
**GBP**) is an implementation of an **Intent System**.

An **Intent System**:

-  is a process around an intent driven data model

-  contains no domain specifics

-  is capable of addressing multiple semantic definitions of intent

To this end, **GBP** Policy views an **Intent System** visually as:

.. figure:: ./images/groupbasedpolicy/IntentSystemPolicySurfaces.png
   :alt: Intent System Process and Policy Surfaces

   Intent System Process and Policy Surfaces

-  **expressed intent** is the entry point into the system.

-  **operational constraints** provide policy for the usage of the
   system which modulates how the system is consumed. For instance *"All
   Financial applications must use a specific encryption standard"*.

-  **capabilities and state** are provided by *renderers*. *Renderers*
   dynamically provide their capabilities to the core model, allowing
   the core model to remain non-domain specific.

-  **governance** provides feedback on the delivery of the *expressed
   intent*. i.e. *"Did we do what you asked us?"*

In summary **GBP is about the Automation of Intent**.

By thinking of **Intent Systems** in this way, it enables:

-  **automation of intent**

   By focusing on **Model. Process. Automation**, a consistent policy
   resolution process enables for mapping between the **expressed
   intent** and renderers responsible for providing the capabilities of
   implementing that intent.

-  recursive/intent level-independent behaviour.

   Where *one person’s concrete is another’s abstract*, intent can be
   fulfilled through a hierarchical implementation of non-domain
   specific policy resolution. Domain specifics are provided by the
   *renderers*, and exposed via the API, at each policy resolution
   instance. For example:

   -  To DNS: The name "www.foo.com" is *abstract*, and it’s IPv4
      address 10.0.0.10 is *concrete*,

   -  To an IP stack: 10.0.0.10 is *abstract* and the MAC
      08:05:04:03:02:01 is *concrete*,

   -  To an Ethernet switch: The MAC 08:05:04:03:02:01 is *abstract*,
      the resolution to a port in it’s CAM table is *concrete*,

   -  To an optical network: The port maybe *abstract*, yet the optical
      wavelength is *concrete*.

    **Note**

    *This is a very domain specific analogy, tied to something most
    readers will understand. It in no way implies the **GBP** should be
    implemented in an OSI type fashion. The premise is that by
    implementing a full **Intent System**, the user is freed from a lot
    of the constraints of how the expressed intent is realised.*

It is important to show the overall philosophy of **GBP** as it sets the
project’s direction.

In the Beryllium release of OpenDaylight, **GBP** focused on **expressed
intent**, **refactoring of how renderers consume and publish Subject
Feature Definitions for multi-renderer support**.

GBP Base Architecture and Value Proposition
-------------------------------------------

Terminology
~~~~~~~~~~~

In order to explain the fundamental value proposition of **GBP**, an
illustrated example is given. In order to do that some terminology must
be defined.

The Access Model is the core of the **GBP** Intent System policy
resolution process.

.. figure:: ./images/groupbasedpolicy/GBPTerminology1.png
   :alt: GBP Access Model Terminology - Endpoints, EndpointGroups,
   Contract

   GBP Access Model Terminology - Endpoints, EndpointGroups, Contract

.. figure:: ./images/groupbasedpolicy/GBPTerminology2.png
   :alt: GBP Access Model Terminology - Subject, Classifier, Action

   GBP Access Model Terminology - Subject, Classifier, Action

.. figure:: ./images/groupbasedpolicy/GBPTerminology3.png
   :alt: GBP Forwarding Model Terminology - L3 Context, L2 Bridge
   Context, L2 Flood Context/Domain, Subnet

   GBP Forwarding Model Terminology - L3 Context, L2 Bridge Context, L2
   Flood Context/Domain, Subnet

-  Endpoints:

   Define concrete uniquely identifiable entities. In Beryllium,
   examples could be a Docker container, or a Neutron port

-  EndpointGroups:

   EndpointGroups are sets of endpoints that share a common set of
   policies. EndpointGroups can participate in contracts that determine
   the kinds of communication that are allowed. EndpointGroups *consume*
   and *provide* contracts. They also expose both *requirements and
   capabilities*, which are labels that help to determine how contracts
   will be applied. An EndpointGroup can specify a parent EndpointGroup
   from which it inherits.

-  Contracts:

   Contracts determine which endpoints can communicate and in what way.
   Contracts between pairs of EndpointGroups are selected by the
   contract selectors defined by the EndpointGroup. Contracts expose
   qualities, which are labels that can help EndpointGroups to select
   contracts. Once the contract is selected, contracts have clauses that
   can match against requirements and capabilities exposed by
   EndpointGroups, as well as any conditions that may be set on
   endpoints, in order to activate subjects that can allow specific
   kinds of communication. A contract is allowed to specify a parent
   contract from which it inherits.

-  Subject

   Subjects describe some aspect of how two endpoints are allowed to
   communicate. Subjects define an ordered list of rules that will match
   against the traffic and perform any necessary actions on that
   traffic. No communication is allowed unless a subject allows that
   communication.

-  Clause

   Clauses are defined as part of a contract. Clauses determine how a
   contract should be applied to particular endpoints and
   EndpointGroups. Clauses can match against requirements and
   capabilities exposed by EndpointGroups, as well as any conditions
   that may be set on endpoints. Matching clauses define some set of
   subjects which can be applied to the communication between the pairs
   of endpoints.

Architecture and Value Proposition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**GBP** offers an intent based interface, accessed via the `UX <#UX>`__,
via the `REST API <#REST>`__ or directly from a domain-specific-language
such as `Neutron <#Neutron>`__ through a mapping interface.

There are two models in **GBP**:

-  the access (or core) model

-  the forwarding model

.. figure:: ./images/groupbasedpolicy/GBP_AccessModel_simple.png
   :alt: GBP Access (or Core) Model

   GBP Access (or Core) Model

The *classifier* and *action* portions of the model can be thought of as
hooks, with their definition provided by each *renderer* about its
domain specific capabilities. In **GBP** Beryllium, there is one
renderer, the *`OpenFlow Overlay renderer (OfOverlay). <#OfOverlay>`__*

These hooks are filled with *definitions* of the types of *features* the
renderer can provide the *subject*, and are called
**subject-feature-definitions**.

This means an *expressed intent* can be fulfilled by, and across,
multiple renderers simultaneously, without any specific provisioning
from the consumer of **GBP**.

Since **GBP** is implemented in OpenDaylight, which is an SDN
controller, it also must address networking. This is done via the
*forwarding model*, which is domain specific to networking, but could be
applied to many different *types* of networking.

.. figure:: ./images/groupbasedpolicy/GBP_ForwardingModel_simple.png
   :alt: GBP Forwarding Model

   GBP Forwarding Model

Each endpoint is provisioned with a *network-containment*. This can be
a:

-  subnet

   -  normal IP stack behaviour, where ARP is performed in subnet, and
      for out of subnet, traffic is sent to default gateway.

   -  a subnet can be a child of any of the below forwarding model
      contexts, but typically would be a child of a flood-domain

-  L2 flood-domain

   -  allows flooding behaviour.

   -  is a n:1 child of a bridge-domain

   -  can have multiple children

-  L2 bridge-domain

   -  is a layer2 namespace

   -  is the realm where traffic can be sent at layer 2

   -  is a n:1 child of a L3 context

   -  can have multiple children

-  L3 context

   -  is a layer3 namespace

   -  is the realm where traffic is passed at layer 3

   -  is a n:1 child of a tenant

   -  can have multiple children

A simple example of how the access and forwarding models work is as
follows:

.. figure:: ./images/groupbasedpolicy/GBP_Endpoint_EPG_Contract.png
   :alt: GBP Endpoints, EndpointGroups and Contracts

   GBP Endpoints, EndpointGroups and Contracts

In this example, the **EPG:webservers** is *providing* the *web* and
*ssh* contracts. The **EPG:client** is consuming those contracts.
**EPG:client** is providing the *any* contract, which is consumed by
**EPG:webservers**.

The *direction* keyword is always from the perspective of the *provider*
of the contract. In this case contract *web*, being *provided* by
**EPG:webservers**, with the classifier to match TCP destination port
80, means:

-  packets with a TCP destination port of 80

-  sent to (*in*) endpoints in the **EPG:webservers**

-  will be *allowed*.

.. figure:: ./images/groupbasedpolicy/GBP_Endpoint_EPG_Forwarding.png
   :alt: GBP Endpoints and the Forwarding Model

   GBP Endpoints and the Forwarding Model

When the forwarding model is considered in the figure above, it can be
seen that even though all endpoints are communicating using a common set
of contracts, their forwarding is *contained* by the forwarding model
contexts or namespaces. In the example shown, the endpoints associated
with a *network-containment* that has an ultimate parent of
*L3Context:Sales* can only communicate with other endpoints within this
L3Context. In this way L3VPN services can be implemented without any
impact to the **Intent** of the contract.

High-level implementation Architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The overall architecture, including *`Neutron <#Neutron>`__* domain
specific mapping, and the `OpenFlow Overlay renderer <#OfOverlay>`__
looks as so:

.. figure:: ./images/groupbasedpolicy/GBP_High-levelBerylliumArchitecture.png
   :alt: GBP High Level Beryllium Architecture

   GBP High Level Beryllium Architecture

The major benefit of this architecture is that the mapping of the
domain-specific-language is completely separate and independent of the
underlying renderer implementation.

For instance, using the `Neutron Mapper <#Neutron>`__, which maps the
Neutron API to the **GBP** core model, any contract automatically
generated from this mapping can be augmented via the `UX <#UX>`__ to use
`Service Function Chaining <#SFC>`__, a capability not currently
available in OpenStack Neutron.

When another renderer is added, for instance, NetConf, the same policy
can now be leveraged across NetConf devices simultaneously:

.. figure:: ./images/groupbasedpolicy/GBP_High-levelExtraRenderer.png
   :alt: GBP High Level Beryllium Architecture - adding a renderer

   GBP High Level Beryllium Architecture - adding a renderer

As other domain-specific mappings occur, they too can leverage the same
renderers, as the renderers only need to implement the **GBP** access
and forwarding models, and the domain-specific mapping need only manage
mapping to the access and forwarding models. For instance:

.. figure:: ./images/groupbasedpolicy/High-levelBerylliumArchitectureEvolution2.png
   :alt: GBP High Level Beryllium Architecture - adding a renderer

   GBP High Level Beryllium Architecture - adding a renderer

In summary, the **GBP** architecture:

-  separates concerns: the Expressed Intent is kept completely separated
   from the underlying renderers.

-  is cohesive: each part does it’s part and it’s part only

-  is scalable: code can be optimised around model
   mapping/implementation, and functionality re-used

Policy Resolution
~~~~~~~~~~~~~~~~~

Contract Selection
^^^^^^^^^^^^^^^^^^

The first step in policy resolution is to select the contracts that are
in scope.

EndpointGroups participate in contracts either as a *provider* or as a
*consumer* of a contract. Each EndpointGroup can participate in many
contracts at the same time, but for each contract it can be in only one
role at a time. In addition, there are two ways for an EndpointGroup to
select a contract: either with either a:

-  *named selector*

   Named selectors simply select a specific contract by its contract ID.

-  target selector.

   Target selectors allow for additional flexibility by matching against
   *qualities* of the contract’s *target.*

Thus, there are a total of 4 kinds of contract selector:

-  provider named selector

   Select a contract by contract ID, and participate as a provider.

-  provider target selector

   Match against a contract’s target with a quality matcher, and
   participate as a provider.

-  consumer named selector

   Select a contract by contract ID, and participate as a consumer.

-  consumer target selector

   Match against a contract’s target with a quality matcher, and
   participate as a consumer.

To determine which contracts are in scope, contracts are found where
either the source EndpointGroup selects a contract as either a provider
or consumer, while the destination EndpointGroup matches against the
same contract in the corresponding role. So if endpoint *x* in
EndpointGroup *X* is communicating with endpoint *y* in EndpointGroup
*Y*, a contract *C* is in scope if either *X* selects *C* as a provider
and *Y* selects *C* as a consumer, or vice versa.

The details of how quality matchers work are described further in
`Matchers <#Matchers>`__. Quality matchers provide a flexible mechanism
for contract selection based on labels.

The end result of the contract selection phase can be thought of as a
set of tuples representing selected contract scopes. The fields of the
tuple are:

-  Contract ID

-  The provider EndpointGroup ID

-  The name of the selector in the provider EndpointGroup that was used
   to select the contract, called the *matching provider selector.*

-  The consumer EndpointGroup ID

-  The name of the selector in the consumer EndpointGroup that was used
   to select the contract, called the *matching consumer selector.*

The result is then stored in the datastore under **Resolved Policy**.

Subject Selection
^^^^^^^^^^^^^^^^^

The second phase in policy resolution is to determine which subjects are
in scope. The subjects define what kinds of communication are allowed
between endpoints in the EndpointGroups. For each of the selected
contract scopes from the contract selection phase, the subject selection
procedure is applied.

Labels called, capabilities, requirements and conditions are matched
against to bring a Subject *into scope*. EndpointGroups have
capabilities and requirements, while endpoints have conditions.

Requirements and Capabilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When acting as a *provider*, EndpointGroups expose *capabilities,* which
are labels representing specific pieces of functionality that can be
exposed to other EndpointGroups that may meet functional requirements of
those EndpointGroups.

When acting as a *consumer*, EndpointGroups expose *requirements*, which
are labels that represent that the EndpointGroup requires some specific
piece of functionality.

As an example, we might create a capability called "user-database" which
indicates that an EndpointGroup contains endpoints that implement a
database of users.

We might create a requirement also called "user-database" to indicate an
EndpointGroup contains endpoints that will need to communicate with the
endpoints that expose this service.

Note that in this example the requirement and capability have the same
name, but the user need not follow this convention.

The matching provider selector (that was used by the provider
EndpointGroup to select the contract) is examined to determine the
capabilities exposed by the provider EndpointGroup for this contract
scope.

The provider selector will have a list of capabilities either directly
included in the provider selector or inherited from a parent selector or
parent EndpointGroup. (See `Inheritance <#Inheritance>`__).

Similarly, the matching consumer selector will expose a set of
requirements.

Conditions
^^^^^^^^^^

Endpoints can have *conditions*, which are labels representing some
relevant piece of operational state related to the endpoint.

An example of a condition might be "malware-detected," or
"authentication-succeeded." Conditions are used to affect how that
particular endpoint can communicate.

To continue with our example, the "malware-detected" condition might
cause an endpoint’s connectivity to be cut off, while
"authentication-succeeded" might open up communication with services
that require an endpoint to be first authenticated and then forward its
authentication credentials.

Clauses
^^^^^^^

Clauses perform the actual selection of subjects. A clause has lists of
matchers in two categories. In order for a clause to become active, all
lists of matchers must match. A matching clause will select all the
subjects referenced by the clause. Note that an empty list of matchers
counts as a match.

The first category is the consumer matchers, which match against the
consumer EndpointGroup and endpoints. The consumer matchers are:

-  Group Idenfication Constraint: Requirement matchers

   Matches against requirements in the matching consumer selector.

-  Group Identification Constraint: GroupName

   Matches against the group name

-  Consumer condition matchers

   Matches against conditions on endpoints in the consumer EndpointGroup

-  Consumer Endpoint Identification Constraint

   Label based criteria for matching against endpoints. In Beryllium
   this can be used to label endpoints based on IpPrefix.

The second category is the provider matchers, which match against the
provider EndpointGroup and endpoints. The provider matchers are:

-  Group Idenfication Constraint: Capability matchers

   Matches against capabilities in the matching provider selector.

-  Group Identification Constraint: GroupName

   Matches against the group name

-  Consumer condition matchers

   Matches against conditions on endpoints in the provider EndpointGroup

-  Consumer Endpoint Identification Constraint

   Label based criteria for matching against endpoints. In Beryllium
   this can be used to label endpoints based on IpPrefix.

Clauses have a list of subjects that apply when all the matchers in the
clause match. The output of the subject selection phase logically is a
set of subjects that are in scope for any particular pair of endpoints.

Rule Application
^^^^^^^^^^^^^^^^

Now subjects have been selected that apply to the traffic between a
particular set of endpoints, policy can be applied to allow endpoints to
communicate. The applicable subjects from the previous step will each
contain a set of rules.

Rules consist of a set of *classifiers* and a set of *actions*.
Classifiers match against traffic between two endpoints. An example of a
classifier would be something that matches against all TCP traffic on
port 80, or one that matches against HTTP traffic containing a
particular cookie. Actions are specific actions that need to be taken on
the traffic before it reaches its destination. Actions could include
tagging or encapsulating the traffic in some way, redirecting the
traffic, or applying a `service function chain <#SFC>`__.

Rules, subjects, and actions have an *order* parameter, where a lower
order value means that a particular item will be applied first. All
rules from a particular subject will be applied before the rules of any
other subject, and all actions from a particular rule will be applied
before the actions from another rule. If more than item has the same
order parameter, ties are broken with a lexicographic ordering of their
names, with earlier names having logically lower order.

Matchers
''''''''

Matchers specify a set of labels (which include requirements,
capabilities, conditions, and qualities) to match against. There are
several kinds of matchers that operate similarly:

-  Quality matchers

   used in target selectors during the contract selection phase. Quality
   matchers provide a more advanced and flexible way to select contracts
   compared to a named selector.

-  Requirement and capability matchers

   used in clauses during the subject selection phase to match against
   requirements and capabilities on EndpointGroups

-  Condition matchers

   used in clauses during the subject selection phase to match against
   conditions on endpoints

A matcher is, at its heart, fairly simple. It will contain a list of
label names, along with a *match type*. The match type can be either:

-  "all"

   which means the matcher matches when all of its labels match

-  "any"

   which means the matcher matches when any of its labels match,

-  "none"

   which means the matcher matches when none of its labels match.

Note a *match all* matcher can be made by matching against an empty set
of labels with a match type of "all."

Additionally each label to match can optionally include a relevant name
field. For quality matchers, this is a target name. For capability and
requirement matchers, this is a selector name. If the name field is
specified, then the matcher will only match against targets or selectors
with that name, rather than any targets or selectors.

Inheritance
^^^^^^^^^^^

Some objects in the system include references to parents, from which
they will inherit definitions. The graph of parent references must be
loop free. When resolving names, the resolution system must detect loops
and raise an exception. Objects that are part of these loops may be
considered as though they are not defined at all. Generally, inheritance
works by simply importing the objects in the parent into the child
object. When there are objects with the same name in the child object,
then the child object will override the parent object according to rules
which are specific to the type of object. We’ll next explore the
detailed rules for inheritance for each type of object

**EndpointGroups**

EndpointGroups will inherit all their selectors from their parent
EndpointGroups. Selectors with the same names as selectors in the parent
EndpointGroups will inherit their behavior as defined below.

**Selectors**

Selectors include provider named selectors, provider target selectors,
consumer named selectors, and consumer target selectors. Selectors
cannot themselves have parent selectors, but when selectors have the
same name as a selector of the same type in the parent EndpointGroup,
then they will inherit from and override the behavior of the selector in
the parent EndpointGroup.

**Named Selectors**

Named selectors will add to the set of contract IDs that are selected by
the parent named selector.

**Target Selectors**

A target selector in the child EndpointGroup with the same name as a
target selector in the parent EndpointGroup will inherit quality
matchers from the parent. If a quality matcher in the child has the same
name as a quality matcher in the parent, then it will inherit as
described below under Matchers.

**Contracts**

Contracts will inherit all their targets, clauses and subjects from
their parent contracts. When any of these objects have the same name as
in the parent contract, then the behavior will be as defined below.

**Targets**

Targets cannot themselves have a parent target, but it may inherit from
targets with the same name as the target in a parent contract. Qualities
in the target will be inherited from the parent. If a quality with the
same name is defined in the child, then this does not have any semantic
effect except if the quality has its inclusion-rule parameter set to
"exclude." In this case, then the label should be ignored for the
purpose of matching against this target.

**Subjects**

Subjects cannot themselves have a parent subject, but it may inherit
from a subject with the same name as the subject in a parent contract.
The order parameter in the child subject, if present, will override the
order parameter in the parent subject. The rules in the parent subject
will be added to the rules in the child subject. However, the rules will
not override rules of the same name. Instead, all rules in the parent
subject will be considered to run with a higher order than all rules in
the child; that is all rules in the child will run before any rules in
the parent. This has the effect of overriding any rules in the parent
without the potentially-problematic semantics of merging the ordering.

**Clauses**

Clauses cannot themselves have a parent clause, but it may inherit from
a clause with the same name as the clause in a parent contract. The list
of subject references in the parent clause will be added to the list of
subject references in the child clause. This is just a union operation.
A subject reference that refers to a subject name in the parent contract
might have that name overridden in the child contract. Each of the
matchers in the clause are also inherited by the child clause. Matchers
in the child of the same name and type as a matcher from the parent will
inherit from and override the parent matcher. See below under Matchers
for more information.

**Matchers**

Matchers include quality matchers, condition matchers, requirement
matchers, and capability matchers. Matchers cannot themselves have
parent matchers, but when there is a matcher of the same name and type
in the parent object, then the matcher in the child object will inherit
and override the behavior of the matcher in the parent object. The match
type, if specified in the child, overrides the value specified in the
parent. Labels are also inherited from the parent object. If there is a
label with the same name in the child object, this does not have any
semantic effect except if the label has its inclusion-rule parameter set
to "exclude." In this case, then the label should be ignored for the
purpose of matching. Otherwise, the label with the same name will
completely override the label from the parent.

Using the GBP UX interface
--------------------------

Overview
~~~~~~~~

These following components make up this application and are described in
more detail in following sections:

-  Basic view

-  Governance view

-  Policy Expression view

-  Wizard view

The **GBP** UX is access via:

::

    http://<odl controller>:8181/index.html

Basic view
~~~~~~~~~~

Basic view contains 5 navigation buttons which switch user to the
desired section of application:

-  Governance – switch to the Governance view (middle of graphic has the
   same function)

-  Renderer configuration – switch to the Policy expression view with
   Renderers section expanded

-  Policy expression – switch to the Policy expression view with Policy
   section expanded

-  Operational constraints – placeholder for development in next release

.. figure:: ./images/groupbasedpolicy/ui-1-basicview.png
   :alt: Basic view

   Basic view

Governance view
~~~~~~~~~~~~~~~

Governance view consists from three columns.

.. figure:: ./images/groupbasedpolicy/ui-2-governanceview.png
   :alt: Governance view

   Governance view

**Governance view – Basic view – Left column**

In the left column is Health section with Exception and Conflict buttons
with no functionality yet. This is a placeholder for development in
further releases.

**Governance view – Basic view – Middle column**

In the top half of this section is select box with list of tenants for
select. Once the tenant is selected, all sub sections in application
operate and display data with actual selected tenant.

Below the select box are buttons which display Expressed or Delivered
policy of Governance section. In the bottom half of this section is
select box with list of renderers for select. There is currently only
`OfOverlay <#OfOverlay>`__ renderer available.

Below the select box is Renderer configuration button, which switch the
app into the Policy expression view with Renderers section expanded for
performing CRUD operations. Renderer state button display Renderer state
view.

**Governance view – Basic view – Right column**

In the bottom part of the right section of Governance view is Home
button which switch the app to the Basic view.

In the top part is situated navigation menu with four main sections.

Policy expression button expand/collapse sub menu with three main parts
of Policy expression. By clicking on sub menu buttons, user will be
switched into the Policy expressions view with appropriate section
expanded for performing CRUD operations.

Renderer configuration button switches user into the Policy expressions
view.

Governance button expand/collapse sub menu with four main parts of
Governance section. Sub menu buttons of Governance section display
appropriate section of Governance view.

Operational constraints have no functionality yet, and is a placeholder
for development in further releases.

Below the menu is place for view info section which displays info about
actual selected element from the topology (explained below).

**Governance view – Expressed policy**

In this view are displayed contracts with their consumed and provided
EndpointGroups of actual selected tenant, which can be changed in select
box in the upper left corner.

By single-clicking on any contract or EPG, the data of actual selected
element will be shown in the right column below the menu. A Manage
button launches a display wizard window for managing configuration of
items such as `Service Function Chaining <#SFC>`__.

.. figure:: ./images/groupbasedpolicy/ui-3-governanceview-expressed.png
   :alt: Expressed policy

   Expressed policy

**Governance view – Delivered policy** In this view are displayed
subjects with their consumed and provided EndpointGroups of actual
selected tenant, which can be changed in select box in the upper left
corner.

By single-clicking on any subject or EPG, the data of actual selected
element will be shown in the right column below the menu.

By double-click on subject the subject detail view will be displayed
with subject’s rules of actual selected subject, which can be changed in
select box in the upper left corner.

By single-clicking on rule or subject, the data of actual selected
element will be shown in the right column below the menu.

By double-clicking on EPG in Delivered policy view, the EPG detail view
will be displayed with EPG’s endpoints of actual selected EPG, which can
be changed in select box in the upper left corner.

By single-clicking on EPG or endpoint the data of actual selected
element will be shown in the right column below the menu.

.. figure:: ./images/groupbasedpolicy/ui-4-governanceview-delivered-0.png
   :alt: Delivered policy

   Delivered policy

.. figure:: ./images/groupbasedpolicy/ui-4-governanceview-delivered-1-subject.png
   :alt: Subject detail

   Subject detail

.. figure:: ./images/groupbasedpolicy/ui-4-governanceview-delivered-2-epg.png
   :alt: EPG detail

   EPG detail

**Governance view – Renderer state**

In this part are displayed Subject feature definition data with two main
parts: Action definition and Classifier definition.

By clicking on the down/right arrow in the circle is possible to
expand/hide data of appropriate container or list. Next to the list node
are displayed names of list’s elements where one is always selected and
element’s data are shown (blue line under the name).

By clicking on names of children nodes is possible to select desired
node and node’s data will be displayed.

.. figure:: ./images/groupbasedpolicy/ui-4-governanceview-renderer.png
   :alt: Renderer state

   Renderer state

Policy expression view
~~~~~~~~~~~~~~~~~~~~~~

In the left part of this view is placed topology of actual selected
elements with the buttons for switching between types of topology at the
bottom.

Right column of this view contains four parts. At the top of this column
are displayed breadcrumbs with actual position in the application.

Below the breadcrumbs is select box with list of tenants for select. In
the middle part is situated navigation menu, which allows switch to the
desired section for performing CRUD operations.

At the bottom is quick navigation menu with Access Model Wizard button
which display Wizard view, Home button which switch application to the
Basic view and occasionally Back button, which switch application to the
upper section.

**Policy expression - Navigation menu**

To open Policy expression, select Policy expression from the GBP Home
screen.

In the top of navigation box you can select the tenant from the tenants
list to activate features addicted to selected tenant.

In the right menu, by default, the Policy menu section is expanded.
Subitems of this section are modules for CRUD (creating, reading,
updating and deleting) of tenants, EndpointGroups, contracts, L2/L3
objects.

-  Section Renderers contains CRUD forms for Classifiers and Actions.

-  Section Endpoints contains CRUD forms for Endpoint and L3 prefix
   endpoint.

.. figure:: ./images/groupbasedpolicy/ui-5-expresssion-1.png
   :alt: Navigation menu

   Navigation menu

.. figure:: ./images/groupbasedpolicy/ui-5-expresssion-2.png
   :alt: CRUD operations

   CRUD operations

**Policy expression - Types of topology**

There are three different types of topology:

-  Configured topology - EndpointGroups and contracts between them from
   CONFIG datastore

-  Operational topology - displays same information but is based on
   operational data.

-  L2/L3 - displays relationships between L3Contexts, L2 Bridge domains,
   L2 Flood domains and Subnets.

.. figure:: ./images/groupbasedpolicy/ui-5-expresssion-3.png
   :alt: L2/L3 Topology

   L2/L3 Topology

.. figure:: ./images/groupbasedpolicy/ui-5-expresssion-4.png
   :alt: Config Topology

   Config Topology

**Policy expression - CRUD operations**

In this part are described basic flows for viewing, adding, editing and
deleting system elements like tenants, EndpointGroups etc.

Tenants
~~~~~~~

To edit tenant objects click the Tenants button in the right menu. You
can see the CRUD form containing tenants list and control buttons.

To add new tenant, click the Add button This will display the form for
adding a new tenant. After filling tenant attributes Name and
Description click Save button. Saving of any object can be performed
only if all the object attributes are filled correctly. If some
attribute doesn’t have correct value, exclamation mark with mouse-over
tooltip will be displayed next to the label for the attribute. After
saving of tenant the form will be closed and the tenants list will be
set to default value.

To view an existing tenant, select the tenant from the select box
Tenants list. The view form is read-only and can be closed by clicking
cross mark in the top right of the form.

To edit selected tenant, click the Edit button, which will display the
edit form for selected tenant. After editing the Name and Description of
selected tenant click the Save button to save selected tenant. After
saving of tenant the edit form will be closed and the tenants list will
be set to default value.

To delete tenant select the tenant from the Tenants list and click
Delete button.

To return to the Policy expression click Back button on the bottom of
window.

**EndpointGroups**

For managing EndpointGroups (EPG) the tenant from the top Tenants list
must be selected.

To add new EPG click Add button and after filling required attributes
click Save button. After adding the EPG you can edit it and assign
Consumer named selector or Provider named selector to it.

To edit EPG click the Edit button after selecting the EPG from Group
list.

To add new Consumer named selector (CNS) click the Add button next to
the Consumer named selectors list. While CNS editing you can set one or
more contracts for current CNS pressing the Plus button and selecting
the contract from the Contracts list. To remove the contract, click on
the cross mark next to the contract. Added CNS can be viewed, edited or
deleted by selecting from the Consumer named selectors list and clicking
the Edit and Delete buttons like with the EPG or tenants.

To add new Provider named selector (PNS) click the Add button next to
the Provider named selectors list. While PNS editing you can set one or
more contracts for current PNS pressing the Plus button and selecting
the contract from the Contracts list. To remove the contract, click on
the cross mark next to the contract. Added PNS can be viewed, edited or
deleted by selecting from the Provider named selectors list and clicking
the Edit and Delete buttons like with the EPG or tenants.

To delete EPG, CNS or PNS select it in selectbox and click the Delete
button next to the selectbox.

**Contracts**

For managing contracts the tenant from the top Tenants list must be
selected.

To add new Contract click Add button and after filling required fields
click Save button.

After adding the Contract user can edit it by selecting in the Contracts
list and clicking Edit button.

To add new Clause click Add button next to the Clause list while editing
the contract. While editing the Clause after selecting clause from the
Clause list user can assign clause subjects by clicking the Plus button
next to the Clause subjects label. Adding and editing action must be
submitted by pressing Save button. To manage Subjects you can use CRUD
form like with the Clause list.

**L2/L3**

For managing L2/L3 the tenant from the top Tenants list must be
selected.

To add L3 Context click the Add button next to the L3 Context list
,which will display the form for adding a new L3 Context. After filling
L3 Context attributes click Save button. After saving of L3 Context,
form will be closed and the L3 Context list will be set to default
value.

To view an existing L3 Context, select the L3 Context from the select
box L3 Context list. The view form is read-only and can be closed by
clicking cross mark in the top right of the form.

If user wants to edit selected L3 Context, click the Edit button, which
will display the edit form for selected L3 Context. After editing click
the Save button to save selected L3 Context. After saving of L3 Context,
the edit form will be closed and the L3 Context list will be set to
default value.

To delete L3 Context, select it from the L3 Context list and click
Delete button.

To add L2 Bridge Domain, click the Add button next to the L2 Bridge
Domain list. This will display the form for adding a new L2 Bridge
Domain. After filling L2 Bridge Domain attributes click Save button.
After saving of L2 Bridge Domain, form will be closed and the L2 Bridge
Domain list will be set to default value.

To view an existing L2 Bridge Domain, select the L2 Bridge Domain from
the select box L2 Bridge Domain list. The view form is read-only and can
be closed by clicking cross mark in the top right of the form.

If user wants to edit selected L2 Bridge Domain, click the Edit button,
which will display the edit form for selected L2 Bridge Domain. After
editing click the Save button to save selected L2 Bridge Domain. After
saving of L2 Bridge Domain the edit form will be closed and the L2
Bridge Domain list will be set to default value.

To delete L2 Bridge Domain select it from the L2 Bridge Domain list and
click Delete button.

To add L3 Flood Domain, click the Add button next to the L3 Flood Domain
list. This will display the form for adding a new L3 Flood Domain. After
filling L3 Flood Domain attributes click Save button. After saving of L3
Flood Domain, form will be closed and the L3 Flood Domain list will be
set to default value.

To view an existing L3 Flood Domain, select the L3 Flood Domain from the
select box L3 Flood Domain list. The view form is read-only and can be
closed by clicking cross mark in the top right of the form.

If user wants to edit selected L3 Flood Domain, click the Edit button,
which will display the edit form for selected L3 Flood Domain. After
editing click the Save button to save selected L3 Flood Domain. After
saving of L3 Flood Domain the edit form will be closed and the L3 Flood
Domain list will be set to default value.

To delete L3 Flood Domain select it from the L3 Flood Domain list and
click Delete button.

To add Subnet click the Add button next to the Subnet list. This will
display the form for adding a new Subnet. After filling Subnet
attributes click Save button. After saving of Subnet, form will be
closed and the Subnet list will be set to default value.

To view an existing Subnet, select the Subnet from the select box Subnet
list. The view form is read-only and can be closed by clicking cross
mark in the top right of the form.

If user wants to edit selected Subnet, click the Edit button, which will
display the edit form for selected Subnet. After editing click the Save
button to save selected Subnet. After saving of Subnet the edit form
will be closed and the Subnet list will be set to default value.

To delete Subnet select it from the Subnet list and click Delete button.

**Classifiers**

To add Classifier, click the Add button next to the Classifier list.
This will display the form for adding a new Classifier. After filling
Classifier attributes click Save button. After saving of Classifier,
form will be closed and the Classifier list will be set to default
value.

To view an existing Classifier, select the Classifier from the select
box Classifier list. The view form is read-only and can be closed by
clicking cross mark in the top right of the form.

If you want to edit selected Classifier, click the Edit button, which
will display the edit form for selected Classifier. After editing click
the Save button to save selected Classifier. After saving of Classifier
the edit form will be closed and the Classifier list will be set to
default value.

To delete Classifier select it from the Classifier list and click Delete
button.

**Actions**

To add Action, click the Add button next to the Action list. This will
display the form for adding a new Action. After filling Action
attributes click Save button. After saving of Action, form will be
closed and the Action list will be set to default value.

To view an existing Action, select the Action from the select box Action
list. The view form is read-only and can be closed by clicking cross
mark in the top right of the form.

If user wants to edit selected Action, click the Edit button, which will
display the edit form for selected Action. After editing click the Save
button to save selected Action. After saving of Action the edit form
will be closed and the Action list will be set to default value.

To delete Action select it from the Action list and click Delete button.

**Endpoint**

To add Endpoint, click the Add button next to the Endpoint list. This
will display the form for adding a new Endpoint. To add EndpointGroup
assignment click the Plus button next to the label EndpointGroups. To
add Condition click Plus button next to the label Condition. To add L3
Address click the Plus button next to the L3 Addresses label. After
filling Endpoint attributes click Save button. After saving of Endpoint,
form will be closed and the Endpoint list will be set to default value.

To view an existing Endpoint just, the Endpoint from the select box
Endpoint list. The view form is read-only and can be closed by clicking
cross mark in the top right of the form.

If you want to edit selected Endpoint, click the Edit button, which will
display the edit form for selected Endpoint. After editing click the
Save button to save selected Endpoint. After saving of Endpoint the edit
form will be closed and the Endpoint list will be set to default value.

To delete Endpoint select it from the Endpoint list and click Delete
button.

**L3 prefix endpoint**

To add L3 prefix endpoint, click the Add button next to the L3 prefix
endpoint list. This will display the form for adding a new Endpoint. To
add EndpointGroup assignment, click the Plus button next to the label
EndpointGroups. To add Condition, click Plus button next to the label
Condition. To add L2 gateway click the Plus button next to the L2
gateways label. To add L3 gateway, click the Plus button next to the L3
gateways label. After filling L3 prefix endpoint attributes click Save
button. After saving of L3 prefix endpoint, form will be closed and the
Endpoint list will be set to default value.

To view an existing L3 prefix endpoint, select the Endpoint from the
select box L3 prefix endpoint list. The view form is read-only and can
be closed by clicking cross mark in the top right of the form.

If you want to edit selected L3 prefix endpoint, click the Edit button,
which will display the edit form for selected L3 prefix endpoint. After
editing click the Save button to save selected L3 prefix endpoint. After
saving of Endpoint the edit form will be closed and the Endpoint list
will be set to default value.

To delete Endpoint select it from the L3 prefix endpoint list and click
Delete button.

Wizard
~~~~~~

Wizard provides quick method to send basic data to controller necessary
for basic usage of GBP application. It is useful in the case that there
aren’t any data in controller. In the first tab is form for create
tenant. The second tab is for CRUD operations with contracts and their
sub elements such as subjects, rules, clauses, action refs and
classifier refs. The last tab is for CRUD operations with EndpointGroups
and their CNS and PNS. Created structure of data is possible to send by
clicking on Submit button.

.. figure:: ./images/groupbasedpolicy/ui-6-wizard.png
   :alt: Wizard

   Wizard

Using the GBP API
-----------------

Please see:

-  `Using the GBP OpenFlow Overlay (OfOverlay) renderer <#OfOverlay>`__

-  `Policy Resolution <#policyresolution>`__

-  `Forwarding Model <#forwarding>`__

-  `the **GBP** demo and development environments for tips <#demo>`__

It is recommended to use either:

-  `Neutron mapper <#Neutron>`__

-  `the UX <#UX>`__

If the REST API must be used, and the above resources are not
sufficient:

-  feature:install odl-dlux-yangui

-  browse to:
   `http://<odl-controller>:8181/index.html <http://<odl-controller>:8181/index.html>`__
   and select YangUI from the left menu.

to explore the various **GBP** REST options

Using OpenStack with GBP
------------------------

Overview
~~~~~~~~

This section is for Application Developers and Network Administrators
who are looking to integrate Group Based Policy with OpenStack.

To enable the **GBP** Neutron Mapper feature, at the Karaf console:

::

    feature:install odl-groupbasedpolicy-neutronmapper

Neutron Mapper has the following dependencies that are automatically
loaded:

::

    odl-neutron-service

Neutron Northbound implementing REST API used by OpenStack

::

    odl-groupbasedpolicy-base

Base **GBP** feature set, such as policy resolution, data model etc.

::

    odl-groupbasedpolicy-ofoverlay

REST calls from OpenStack Neutron are by the Neutron NorthBound project.

**GBP** provides the implementation of the `Neutron V2.0
API <http://developer.openstack.org/api-ref-networking-v2.html>`__.

Features
~~~~~~~~

List of supported Neutron entities:

-  Port

-  Network

   -  Standard Internal

   -  External provider L2/L3 network

-  Subnet

-  Security-groups

-  Routers

   -  Distributed functionality with local routing per compute

   -  External gateway access per compute node (dedicated port required)

   -  Multiple routers per tenant

-  FloatingIP NAT

-  IPv4/IPv6 support

The mapping of Neutron entities to **GBP** entities is as follows:

**Neutron Port**

.. figure:: ./images/groupbasedpolicy/neutronmapper-gbp-mapping-port.png
   :alt: Neutron Port

   Neutron Port

The Neutron port is mapped to an endpoint.

The current implementation supports one IP address per Neutron port.

An endpoint and L3-endpoint belong to multiple EndpointGroups if the
Neutron port is in multiple Neutron Security Groups.

The key for endpoint is L2-bridge-domain obtained as the parent of
L2-flood-domain representing Neutron network. The MAC address is from
the Neutron port. An L3-endpoint is created based on L3-context (the
parent of the L2-bridge-domain) and IP address of Neutron Port.

**Neutron Network**

.. figure:: ./images/groupbasedpolicy/neutronmapper-gbp-mapping-network.png
   :alt: Neutron Network

   Neutron Network

A Neutron network has the following characteristics:

-  defines a broadcast domain

-  defines a L2 transmission domain

-  defines a L2 name space.

To represent this, a Neutron Network is mapped to multiple **GBP**
entities. The first mapping is to an L2 flood-domain to reflect that the
Neutron network is one flooding or broadcast domain. An L2-bridge-domain
is then associated as the parent of L2 flood-domain. This reflects both
the L2 transmission domain as well as the L2 addressing namespace.

The third mapping is to L3-context, which represents the distinct L3
address space. The L3-context is the parent of L2-bridge-domain.

**Neutron Subnet**

.. figure:: ./images/groupbasedpolicy/neutronmapper-gbp-mapping-subnet.png
   :alt: Neutron Subnet

   Neutron Subnet

Neutron subnet is associated with a Neutron network. The Neutron subnet
is mapped to a **GBP** subnet where the parent of the subnet is
L2-flood-domain representing the Neutron network.

**Neutron Security Group**

.. figure:: ./images/groupbasedpolicy/neutronmapper-gbp-mapping-securitygroup.png
   :alt: Neutron Security Group and Rules

   Neutron Security Group and Rules

**GBP** entity representing Neutron security-group is EndpointGroup.

**Infrastructure EndpointGroups**

Neutron-mapper automatically creates EndpointGroups to manage key
infrastructure items such as:

-  DHCP EndpointGroup - contains endpoints representing Neutron DHCP
   ports

-  Router EndpointGroup - contains endpoints representing Neutron router
   interfaces

-  External EndpointGroup - holds L3-endpoints representing Neutron
   router gateway ports, also associated with FloatingIP ports.

**Neutron Security Group Rules**

This is the most involved amongst all the mappings because Neutron
security-group-rules are mapped to contracts with clauses, subjects,
rules, action-refs, classifier-refs, etc. Contracts are used between
EndpointGroups representing Neutron Security Groups. For simplification
it is important to note that Neutron security-group-rules are similar to
a **GBP** rule containing:

-  classifier with direction

-  action of **allow**.

**Neutron Routers**

.. figure:: ./images/groupbasedpolicy/neutronmapper-gbp-mapping-router.png
   :alt: Neutron Router

   Neutron Router

Neutron router is represented as a L3-context. This treats a router as a
Layer3 namespace, and hence every network attached to it a part of that
Layer3 namespace.

This allows for multiple routers per tenant with complete isolation.

The mapping of the router to an endpoint represents the router’s
interface or gateway port.

The mapping to an EndpointGroup represents the internal infrastructure
EndpointGroups created by the **GBP** Neutron Mapper

When a Neutron router interface is attached to a network/subnet, that
network/subnet and its associated endpoints or Neutron Ports are
seamlessly added to the namespace.

**Neutron FloatingIP**

When associated with a Neutron Port, this leverages the
`OfOverlay <#OfOverlay>`__ renderer’s NAT capabilities.

A dedicated *external* interface on each Nova compute host allows for
disitributed external access. Each Nova instance associated with a
FloatingIP address can access the external network directly without
having to route via the Neutron controller, or having to enable any form
of Neutron distributed routing functionality.

Assuming the gateway provisioned in the Neutron Subnet command for the
external network is reachable, the combination of **GBP** Neutron Mapper
and `OfOverlay renderer <#OfOverlay>`__ will automatically ARP for this
default gateway, requiring no user intervention.

**Troubleshooting within GBP**

Logging level for the mapping functionality can be set for package
org.opendaylight.groupbasedpolicy.neutron.mapper. An example of enabling
TRACE logging level on Karaf console:

::

    log:set TRACE org.opendaylight.groupbasedpolicy.neutron.mapper

**Neutron mapping example**

As an example for mapping can be used creation of Neutron network,
subnet and port. When a Neutron network is created 3 **GBP** entities
are created: l2-flood-domain, l2-bridge-domain, l3-context.

.. figure:: ./images/groupbasedpolicy/neutronmapper-gbp-mapping-network-example.png
   :alt: Neutron network mapping

   Neutron network mapping

After an subnet is created in the network mapping looks like this.

.. figure:: ./images/groupbasedpolicy/neutronmapper-gbp-mapping-subnet-example.png
   :alt: Neutron subnet mapping

   Neutron subnet mapping

If an Neutron port is created in the subnet an endpoint and l3-endpoint
are created. The endpoint has key composed from l2-bridge-domain and MAC
address from Neutron port. A key of l3-endpoint is compesed from
l3-context and IP address. The network containment of endpoint and
l3-endpoint points to the subnet.

.. figure:: ./images/groupbasedpolicy/neutronmapper-gbp-mapping-port-example.png
   :alt: Neutron port mapping

   Neutron port mapping

Configuring GBP Neutron
~~~~~~~~~~~~~~~~~~~~~~~

No intervention passed initial OpenStack setup is required by the user.

More information about configuration can be found in our DevStack demo
environment on the `**GBP**
wiki <https://wiki.opendaylight.org/view/Group_Based_Policy_(GBP)>`__.

Administering or Managing GBP Neutron
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For consistencies sake, all provisioning should be performed via the
Neutron API. (CLI or Horizon).

The mapped policies can be augmented via the **GBP** `UX <#UX>`__, to:

-  Enable `Service Function Chaining <#SFC>`__

-  Add endpoints from outside of Neutron i.e. VMs/containers not
   provisioned in OpenStack

-  Augment policies/contracts derived from Security Group Rules

-  Overlay additional contracts or groupings

Tutorials
~~~~~~~~~

A DevStack demo environment can be found on the `**GBP**
wiki <https://wiki.opendaylight.org/view/Group_Based_Policy_(GBP)>`__.

Using the GBP OpenFlow Overlay (OfOverlay) renderer
---------------------------------------------------

Overview
~~~~~~~~

The OpenFlow Overlay (OfOverlay) feature enables the OpenFlow Overlay
renderer, which creates a network virtualization solution across nodes
that host Open vSwitch software switches.

Installing and Pre-requisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the Karaf console in OpenDaylight:

::

    feature:install odl-groupbasedpolicy-ofoverlay

This renderer is designed to work with OpenVSwitch (OVS) 2.1+ (although
2.3 is strongly recommended) and OpenFlow 1.3.

When used in conjunction with the `Neutron Mapper feature <#Neutron>`__
no extra OfOverlay specific setup is required.

When this feature is loaded "standalone", the user is required to
configure infrastructure, such as

-  instantiating OVS bridges,

-  attaching hosts to the bridges,

-  and creating the VXLAN/VXLAN-GPE tunnel ports on the bridges.

The **GBP** OfOverlay renderer also supports a table offset option, to
offset the pipeline post-table 0. The value of table offset is stored in
the config datastore and it may be rewritten at runtime.

::

    PUT http://{{controllerIp}}:8181/restconf/config/ofoverlay:of-overlay-config
    {
        "of-overlay-config": {
            "gbp-ofoverlay-table-offset": 6
        }
    }

The default value is set by changing:
<gbp-ofoverlay-table-offset>0</gbp-ofoverlay-table-offset>

in file:
distribution-karaf/target/assembly/etc/opendaylight/karaf/15-groupbasedpolicy-ofoverlay.xml

To avoid overwriting runtime changes, the default value is used only
when the OfOverlay renderer starts and no other value has been written
before.

OpenFlow Overlay Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are the primary components of **GBP**. The OfOverlay components
are highlighted in red.

.. figure:: ./images/groupbasedpolicy/ofoverlay-1-components.png
   :alt: OfOverlay within **GBP**

   OfOverlay within **GBP**

In terms of the inner components of the **GBP** OfOverlay renderer:

.. figure:: ./images/groupbasedpolicy/ofoverlay-2-components.png
   :alt: OfOverlay expanded view:

   OfOverlay expanded view:

**OfOverlay Renderer**

Launches components below:

**Policy Resolver**

Policy resolution is completely domain independent, and the OfOverlay
leverages process policy information internally. See `Policy Resolution
process <#policyresolution>`__.

It listens to inputs to the *Tenants* configuration datastore, validates
tenant input, then writes this to the Tenants operational datastore.

From there an internal notification is generated to the PolicyManager.

In the next release, this will be moving to a non-renderer specific
location.

**Endpoint Manager**

The endpoint repository operates in **orchestrated** mode. This means
the user is responsible for the provisioning of endpoints via:

-  `UX/GUI <#UX>`__

-  REST API

    **Note**

    When using the `Neutron mapper <#Neutron>`__ feature, everything is
    managed transparently via Neutron.

The Endpoint Manager is responsible for listening to Endpoint repository
updates and notifying the Switch Manager when a valid Endpoint has been
registered.

It also supplies utility functions to the flow pipeline process.

**Switch Manager**

The Switch Manager is purely a state manager.

Switches are in one of 3 states:

-  DISCONNECTED

-  PREPARING

-  READY

**Ready** is denoted by a connected switch:

-  having a tunnel interface

-  having at least one endpoint connected.

In this way **GBP** is not writing to switches it has no business to.

**Preparing** simply means the switch has a controller connection but is
missing one of the above *complete and necessary* conditions

**Disconnected** means a previously connected switch is no longer
present in the Inventory operational datastore.

.. figure:: ./images/groupbasedpolicy/ofoverlay-3-flowpipeline.png
   :alt: OfOverlay Flow Pipeline

   OfOverlay Flow Pipeline

The OfOverlay leverages Nicira registers as follows:

-  REG0 = Source EndpointGroup + Tenant ordinal

-  REG1 = Source Conditions + Tenant ordinal

-  REG2 = Destination EndpointGroup + Tenant ordinal

-  REG3 = Destination Conditions + Tenant ordinal

-  REG4 = Bridge Domain + Tenant ordinal

-  REG5 = Flood Domain + Tenant ordinal

-  REG6 = Layer 3 Context + Tenant ordinal

**Port Security**

Table 0 of the OpenFlow pipeline. Responsible for ensuring that only
valid connections can send packets into the pipeline:

::

    cookie=0x0, <snip> , priority=200,in_port=3 actions=goto_table:2
    cookie=0x0, <snip> , priority=200,in_port=1 actions=goto_table:1
    cookie=0x0, <snip> , priority=121,arp,in_port=5,dl_src=fa:16:3e:d5:b9:8d,arp_spa=10.1.1.3 actions=goto_table:2
    cookie=0x0, <snip> , priority=120,ip,in_port=5,dl_src=fa:16:3e:d5:b9:8d,nw_src=10.1.1.3 actions=goto_table:2
    cookie=0x0, <snip> , priority=115,ip,in_port=5,dl_src=fa:16:3e:d5:b9:8d,nw_dst=255.255.255.255 actions=goto_table:2
    cookie=0x0, <snip> , priority=112,ipv6 actions=drop
    cookie=0x0, <snip> , priority=111, ip actions=drop
    cookie=0x0, <snip> , priority=110,arp actions=drop
    cookie=0x0, <snip> ,in_port=5,dl_src=fa:16:3e:d5:b9:8d actions=goto_table:2
    cookie=0x0, <snip> , priority=1 actions=drop

Ingress from tunnel interface, go to Table *Source Mapper*:

::

    cookie=0x0, <snip> , priority=200,in_port=3 actions=goto_table:2

Ingress from outside, goto Table *Ingress NAT Mapper*:

::

    cookie=0x0, <snip> , priority=200,in_port=1 actions=goto_table:1

ARP from Endpoint, go to Table *Source Mapper*:

::

    cookie=0x0, <snip> , priority=121,arp,in_port=5,dl_src=fa:16:3e:d5:b9:8d,arp_spa=10.1.1.3 actions=goto_table:2

IPv4 from Endpoint, go to Table *Source Mapper*:

::

    cookie=0x0, <snip> , priority=120,ip,in_port=5,dl_src=fa:16:3e:d5:b9:8d,nw_src=10.1.1.3 actions=goto_table:2

DHCP DORA from Endpoint, go to Table *Source Mapper*:

::

    cookie=0x0, <snip> , priority=115,ip,in_port=5,dl_src=fa:16:3e:d5:b9:8d,nw_dst=255.255.255.255 actions=goto_table:2

Series of DROP tables with priority set to capture any non-specific
traffic that should have matched above:

::

    cookie=0x0, <snip> , priority=112,ipv6 actions=drop
    cookie=0x0, <snip> , priority=111, ip actions=drop
    cookie=0x0, <snip> , priority=110,arp actions=drop

"L2" catch all traffic not identified above:

::

    cookie=0x0, <snip> ,in_port=5,dl_src=fa:16:3e:d5:b9:8d actions=goto_table:2

Drop Flow:

::

    cookie=0x0, <snip> , priority=1 actions=drop

**Ingress NAT Mapper**

Table `*offset* <#offset>`__\ +1.

ARP responder for external NAT address:

::

    cookie=0x0, <snip> , priority=150,arp,arp_tpa=192.168.111.51,arp_op=1 actions=move:NXM_OF_ETH_SRC[]->NXM_OF_ETH_DST[],set_field:fa:16:3e:58:c3:dd->eth_src,load:0x2->NXM_OF_ARP_OP[],move:NXM_NX_ARP_SHA[]->NXM_NX_ARP_THA[],load:0xfa163e58c3dd->NXM_NX_ARP_SHA[],move:NXM_OF_ARP_SPA[]->NXM_OF_ARP_TPA[],load:0xc0a86f33->NXM_OF_ARP_SPA[],IN_PORT

Translate from Outside to Inside and perform same functions as
SourceMapper.

::

    cookie=0x0, <snip> , priority=100,ip,nw_dst=192.168.111.51 actions=set_field:10.1.1.2->ip_dst,set_field:fa:16:3e:58:c3:dd->eth_dst,load:0x2->NXM_NX_REG0[],load:0x1->NXM_NX_REG1[],load:0x4->NXM_NX_REG4[],load:0x5->NXM_NX_REG5[],load:0x7->NXM_NX_REG6[],load:0x3->NXM_NX_TUN_ID[0..31],goto_table:3

**Source Mapper**

Table `*offset* <#offset>`__\ +2.

Determines based on characteristics from the ingress port, which:

-  EndpointGroup(s) it belongs to

-  Forwarding context

-  Tunnel VNID ordinal

Establishes tunnels at valid destination switches for ingress.

Ingress Tunnel established at remote node with VNID Ordinal that maps to
Source EPG, Forwarding Context etc:

::

    cookie=0x0, <snip>, priority=150,tun_id=0xd,in_port=3 actions=load:0xc->NXM_NX_REG0[],load:0xffffff->NXM_NX_REG1[],load:0x4->NXM_NX_REG4[],load:0x5->NXM_NX_REG5[],load:0x7->NXM_NX_REG6[],goto_table:3

Maps endpoint to Source EPG, Forwarding Context based on ingress port,
and MAC:

::

    cookie=0x0, <snip> , priority=100,in_port=5,dl_src=fa:16:3e:b4:b4:b1 actions=load:0xc->NXM_NX_REG0[],load:0x1->NXM_NX_REG1[],load:0x4->NXM_NX_REG4[],load:0x5->NXM_NX_REG5[],load:0x7->NXM_NX_REG6[],load:0xd->NXM_NX_TUN_ID[0..31],goto_table:3

Generic drop:

::

    cookie=0x0, duration=197.622s, table=2, n_packets=0, n_bytes=0, priority=1 actions=drop

**Destination Mapper**

Table `*offset* <#offset>`__\ +3.

Determines based on characteristics of the endpoint:

-  EndpointGroup(s) it belongs to

-  Forwarding context

-  Tunnel Destination value

Manages routing based on valid ingress nodes ARP’ing for their default
gateway, and matches on either gateway MAC or destination endpoint MAC.

ARP for default gateway for the 10.1.1.0/24 subnet:

::

    cookie=0x0, <snip> , priority=150,arp,reg6=0x7,arp_tpa=10.1.1.1,arp_op=1 actions=move:NXM_OF_ETH_SRC[]->NXM_OF_ETH_DST[],set_field:fa:16:3e:28:4c:82->eth_src,load:0x2->NXM_OF_ARP_OP[],move:NXM_NX_ARP_SHA[]->NXM_NX_ARP_THA[],load:0xfa163e284c82->NXM_NX_ARP_SHA[],move:NXM_OF_ARP_SPA[]->NXM_OF_ARP_TPA[],load:0xa010101->NXM_OF_ARP_SPA[],IN_PORT

Broadcast traffic destined for GroupTable:

::

    cookie=0x0, <snip> , priority=140,reg5=0x5,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00 actions=load:0x5->NXM_NX_TUN_ID[0..31],group:5

Layer3 destination matching flows, where priority=100+masklength. Since
**GBP** now support L3Prefix endpoint, we can set default routes etc:

::

    cookie=0x0, <snip>, priority=132,ip,reg6=0x7,dl_dst=fa:16:3e:b4:b4:b1,nw_dst=10.1.1.3 actions=load:0xc->NXM_NX_REG2[],load:0x1->NXM_NX_REG3[],load:0x5->NXM_NX_REG7[],set_field:fa:16:3e:b4:b4:b1->eth_dst,dec_ttl,goto_table:4

Layer2 destination matching flows, designed to be caught only after last
IP flow (lowest priority IP flow is 100):

::

    cookie=0x0, duration=323.203s, table=3, n_packets=4, n_bytes=168, priority=50,reg4=0x4,dl_dst=fa:16:3e:58:c3:dd actions=load:0x2->NXM_NX_REG2[],load:0x1->NXM_NX_REG3[],load:0x2->NXM_NX_REG7[],goto_table:4

General drop flow: cookie=0x0, duration=323.207s, table=3, n\_packets=6,
n\_bytes=588, priority=1 actions=drop

**Policy Enforcer**

Table `*offset* <#offset>`__\ +4.

Once the Source and Destination EndpointGroups are assigned, policy is
enforced based on resolved rules.

In the case of `Service Function Chaining <#SFC>`__, the encapsulation
and destination for traffic destined to a chain, is discovered and
enforced.

Policy flow, allowing IP traffic between EndpointGroups:

::

    cookie=0x0, <snip> , priority=64998,ip,reg0=0x8,reg1=0x1,reg2=0xc,reg3=0x1 actions=goto_table:5

**Egress NAT Mapper**

Table `*offset* <#offset>`__\ +5.

Performs NAT function before Egressing OVS instance to the underlay
network.

Inside to Outside NAT translation before sending to underlay:

::

    cookie=0x0, <snip> , priority=100,ip,reg6=0x7,nw_src=10.1.1.2 actions=set_field:192.168.111.51->ip_src,goto_table:6

**External Mapper**

Table `*offset* <#offset>`__\ +6.

Manages post-policy enforcement for endpoint specific destination
effects. Specifically for `Service Function Chaining <#SFC>`__, which is
why we can support both symmetric and asymmetric chains and distributed
ingress/egress classification.

Generic allow:

::

    cookie=0x0, <snip>, priority=100 actions=output:NXM_NX_REG7[]

Configuring OpenFlow Overlay via REST
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    **Note**

    Please see the `UX <#UX>`__ section on how to configure **GBP** via
    the GUI.

**Endpoint**

::

    POST http://{{controllerIp}}:8181/restconf/operations/endpoint:register-endpoint
    {
        "input": {
            "endpoint-group": "<epg0>",
            "endpoint-groups" : ["<epg1>","<epg2>"],
            "network-containment" : "<fowarding-model-context1>",
            "l2-context": "<bridge-domain1>",
            "mac-address": "<mac1>",
            "l3-address": [
                {
                    "ip-address": "<ipaddress1>",
                    "l3-context": "<l3_context1>"
                }
            ],
            "*ofoverlay:port-name*": "<ovs port name>",
            "tenant": "<tenant1>"
        }
    }

    **Note**

    The usage of "port-name" preceded by "ofoverlay". In OpenDaylight,
    base datastore objects can be *augmented*. In **GBP**, the base
    endpoint model has no renderer specifics, hence can be leveraged
    across multiple renderers.

**OVS Augmentations to Inventory**

::

    PUT http://{{controllerIp}}:8181/restconf/config/opendaylight-inventory:nodes/
    {
        "opendaylight-inventory:nodes": {
            "node": [
                {
                    "id": "openflow:123456",
                    "ofoverlay:tunnel": [
                        {
                            "tunnel-type": "overlay:tunnel-type-vxlan",
                            "ip": "<ip_address_of_ovs>",
                            "port": 4789,
                            "node-connector-id": "openflow:123456:1"
                        }
                    ]
                },
                {
                    "id": "openflow:654321",
                    "ofoverlay:tunnel": [
                        {
                            "tunnel-type": "overlay:tunnel-type-vxlan",
                            "ip": "<ip_address_of_ovs>",
                            "port": 4789,
                            "node-connector-id": "openflow:654321:1"
                        }
                    ]
                }
            ]
        }
    }

**Tenants** see `Policy Resolution <#policyresolution>`__ and
`Forwarding Model <#forwarding>`__ for details:

::

    {
      "policy:tenant": {
        "contract": [
          {
            "clause": [
              {
                "name": "allow-http-clause",
                "subject-refs": [
                  "allow-http-subject",
                  "allow-icmp-subject"
                ]
              }
            ],
            "id": "<id>",
            "subject": [
              {
                "name": "allow-http-subject",
                "rule": [
                  {
                    "classifier-ref": [
                      {
                        "direction": "in",
                        "name": "http-dest"
                      },
                      {
                        "direction": "out",
                        "name": "http-src"
                      }
                    ],
                    "action-ref": [
                      {
                        "name": "allow1",
                        "order": 0
                      }
                    ],
                    "name": "allow-http-rule"
                  }
                ]
              },
              {
                "name": "allow-icmp-subject",
                "rule": [
                  {
                    "classifier-ref": [
                      {
                        "name": "icmp"
                      }
                    ],
                    "action-ref": [
                      {
                        "name": "allow1",
                        "order": 0
                      }
                    ],
                    "name": "allow-icmp-rule"
                  }
                ]
              }
            ]
          }
        ],
        "endpoint-group": [
          {
            "consumer-named-selector": [
              {
                "contract": [
                  "<id>"
                ],
                "name": "<name>"
              }
            ],
            "id": "<id>",
            "provider-named-selector": []
          },
          {
            "consumer-named-selector": [],
            "id": "<id>",
            "provider-named-selector": [
              {
                "contract": [
                  "<id>"
                ],
                "name": "<name>"
              }
            ]
          }
        ],
        "id": "<id>",
        "l2-bridge-domain": [
          {
            "id": "<id>",
            "parent": "<id>"
          }
        ],
        "l2-flood-domain": [
          {
            "id": "<id>",
            "parent": "<id>"
          },
          {
            "id": "<id>",
            "parent": "<id>"
          }
        ],
        "l3-context": [
          {
            "id": "<id>"
          }
        ],
        "name": "GBPPOC",
        "subject-feature-instances": {
          "classifier-instance": [
            {
              "classifier-definition-id": "<id>",
              "name": "http-dest",
              "parameter-value": [
                {
                  "int-value": "6",
                  "name": "proto"
                },
                {
                  "int-value": "80",
                  "name": "destport"
                }
              ]
            },
            {
              "classifier-definition-id": "<id>",
              "name": "http-src",
              "parameter-value": [
                {
                  "int-value": "6",
                  "name": "proto"
                },
                {
                  "int-value": "80",
                  "name": "sourceport"
                }
              ]
            },
            {
              "classifier-definition-id": "<id>",
              "name": "icmp",
              "parameter-value": [
                {
                  "int-value": "1",
                  "name": "proto"
                }
              ]
            }
          ],
          "action-instance": [
            {
              "name": "allow1",
              "action-definition-id": "<id>"
            }
          ]
        },
        "subnet": [
          {
            "id": "<id>",
            "ip-prefix": "<ip_prefix>",
            "parent": "<id>",
            "virtual-router-ip": "<ip address>"
          },
          {
            "id": "<id>",
            "ip-prefix": "<ip prefix>",
            "parent": "<id>",
            "virtual-router-ip": "<ip address>"
          }
        ]
      }
    }

Tutorials
~~~~~~~~~

Comprehensive tutorials, along with a demonstration environment
leveraging Vagrant can be found on the `**GBP**
wiki <https://wiki.opendaylight.org/view/Group_Based_Policy_(GBP)>`__

Using the GBP eBPF IO Visor Agent renderer
------------------------------------------

Overview
~~~~~~~~

The IO Visor renderer feature enables container endpoints (e.g. Docker,
LXC) to leverage GBP policies.

The renderer interacts with a IO Visor module from the Linux Foundation
IO Visor project.

Installing and Pre-requisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the Karaf console in OpenDaylight:

::

    feature:install odl-groupbasedpolicy-iovisor odl-restconf

Installation details, usage, and other information for the IO Visor GBP
module can be found here: `**IO Visor** github repo for IO
Modules <https://github.com/iovisor/iomodules>`__

Using the GBP FaaS renderer
---------------------------

Overview
~~~~~~~~

The FaaS renderer feature enables leveraging the FaaS project as a GBP
renderer.

Installing and Pre-requisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From the Karaf console in OpenDaylight:

::

    feature:install odl-groupbasedpolicy-faas

More information about FaaS can be found here:
https://wiki.opendaylight.org/view/FaaS:GBPIntegration

Using Service Function Chaining (SFC) with GBP Neutron Mapper and OfOverlay
---------------------------------------------------------------------------

Overview
~~~~~~~~

Please refer to the Service Function Chaining project for specifics on
SFC provisioning and theory.

**GBP** allows for the use of a chain, by name, in policy.

This takes the form of an *action* in **GBP**.

Using the `**GBP** demo and development environment <#demo>`__ as an
example:

.. figure:: ./images/groupbasedpolicy/sfc-1-topology.png
   :alt: GBP and SFC integration environment

   GBP and SFC integration environment

In the topology above, a symmetrical chain between H35\_2 and H36\_3
could take path:

H35\_2 to sw1 to sff1 to sf1 to sff1 to sff2 to sf2 to sff2 to sw6 to
H36\_3

If symmetric chaining was desired, the return path is:

.. figure:: ./images/groupbasedpolicy/sfc-2-symmetric.png
   :alt: GBP and SFC symmetric chain environment

   GBP and SFC symmetric chain environment

If asymmetric chaining was desired, the return path could be direct, or
an **entirely different chain**.

.. figure:: ./images/groupbasedpolicy/sfc-3-asymmetric.png
   :alt: GBP and SFC assymmetric chain environment

   GBP and SFC assymmetric chain environment

All these scenarios are supported by the integration.

In the **Subject Feature Instance** section of the tenant config, we
define the instances of the classifier definitions for ICMP and HTTP:

::

            "subject-feature-instances": {
              "classifier-instance": [
                {
                  "name": "icmp",
                  "parameter-value": [
                    {
                      "name": "proto",
                      "int-value": 1
                    }
                  ]
                },
                {
                  "name": "http-dest",
                  "parameter-value": [
                    {
                      "int-value": "6",
                      "name": "proto"
                    },
                    {
                      "int-value": "80",
                      "name": "destport"
                    }
                  ]
                },
                {
                  "name": "http-src",
                  "parameter-value": [
                    {
                      "int-value": "6",
                      "name": "proto"
                    },
                    {
                      "int-value": "80",
                      "name": "sourceport"
                    }
                  ]
                }
              ],

Then the action instances to associate to traffic that matches
classifiers are defined.

Note the *SFC chain name* must exist in SFC, and is validated against
the datastore once the tenant configuration is entered, before entering
a valid tenant configuration into the operational datastore (which
triggers policy resolution).

::

              "action-instance": [
                {
                  "name": "chain1",
                  "parameter-value": [
                    {
                      "name": "sfc-chain-name",
                      "string-value": "SFCGBP"
                    }
                  ]
                },
                {
                  "name": "allow1",
                }
              ]
            },

When ICMP is matched, allow the traffic:

::

            "contract": [
              {
                "subject": [
                  {
                    "name": "icmp-subject",
                    "rule": [
                      {
                        "name": "allow-icmp-rule",
                        "order" : 0,
                        "classifier-ref": [
                          {
                            "name": "icmp"
                          }
                        ],
                        "action-ref": [
                          {
                            "name": "allow1",
                            "order": 0
                          }
                        ]
                      }

                    ]
                  },

When HTTP is matched, **in** to the provider of the contract with a TCP
destination port of 80 (HTTP) or the HTTP request. The chain action is
triggered, and similarly **out** from the provider for traffic with TCP
source port of 80 (HTTP), or the HTTP response.

::

                  {
                    "name": "http-subject",
                    "rule": [
                      {
                        "name": "http-chain-rule-in",
                        "classifier-ref": [
                          {
                            "name": "http-dest",
                            "direction": "in"
                          }
                        ],
                        "action-ref": [
                          {
                            "name": "chain1",
                            "order": 0
                          }
                        ]
                      },
                      {
                        "name": "http-chain-rule-out",
                        "classifier-ref": [
                          {
                            "name": "http-src",
                            "direction": "out"
                          }
                        ],
                        "action-ref": [
                          {
                            "name": "chain1",
                            "order": 0
                          }
                        ]
                      }
                    ]
                  }

To enable asymmetrical chaining, for instance, the user desires that
HTTP requests traverse the chain, but the HTTP response does not, the
HTTP response is set to *allow* instead of chain:

::

                      {
                        "name": "http-chain-rule-out",
                        "classifier-ref": [
                          {
                            "name": "http-src",
                            "direction": "out"
                          }
                        ],
                        "action-ref": [
                          {
                            "name": "allow1",
                            "order": 0
                          }
                        ]
                      }

Demo/Development environment
----------------------------

The **GBP** project for Beryllium has two demo/development environments.

-  Docker based GBP and GBP+SFC integration Vagrant environment

-  DevStack based GBP+Neutron integration Vagrant environment

`Demo @ GBP
wiki <https://wiki.opendaylight.org/view/Group_Based_Policy_(GBP)/Consumability/Demo>`__

L2Switch User Guide
===================

Overview
--------

The L2Switch project provides Layer2 switch functionality.

L2Switch Architecture
---------------------

-  Packet Handler

   -  Decodes the packets coming to the controller and dispatches them
      appropriately

-  Loop Remover

   -  Removes loops in the network

-  Arp Handler

   -  Handles the decoded ARP packets

-  Address Tracker

   -  Learns the Addresses (MAC and IP) of entities in the network

-  Host Tracker

   -  Tracks the locations of hosts in the network

-  L2Switch Main

   -  Installs flows on each switch based on network traffic

Configuring L2Switch
--------------------

This sections below give details about the configuration settings for
the components that can be configured.

Configuring Loop Remover
------------------------

-  52-loopremover.xml

   -  is-install-lldp-flow

      -  "true" means a flow that sends all LLDP packets to the
         controller will be installed on each switch

      -  "false" means this flow will not be installed

   -  lldp-flow-table-id

      -  The LLDP flow will be installed on the specified flow table of
         each switch

      -  This field is only relevant when "is-install-lldp-flow" is set
         to "true"

   -  lldp-flow-priority

      -  The LLDP flow will be installed with the specified priority

      -  This field is only relevant when "is-install-lldp-flow" is set
         to "true"

   -  lldp-flow-idle-timeout

      -  The LLDP flow will timeout (removed from the switch) if the
         flow doesn’t forward a packet for *x* seconds

      -  This field is only relevant when "is-install-lldp-flow" is set
         to "true"

   -  lldp-flow-hard-timeout

      -  The LLDP flow will timeout (removed from the switch) after *x*
         seconds, regardless of how many packets it is forwarding

      -  This field is only relevant when "is-install-lldp-flow" is set
         to "true"

   -  graph-refresh-delay

      -  A graph of the network is maintained and gets updated as
         network elements go up/down (i.e. links go up/down and switches
         go up/down)

      -  After a network element going up/down, it waits
         *graph-refresh-delay* seconds before recomputing the graph

      -  A higher value has the advantage of doing less graph updates,
         at the potential cost of losing some packets because the graph
         didn’t update immediately.

      -  A lower value has the advantage of handling network topology
         changes quicker, at the cost of doing more computation.

Configuring Arp Handler
-----------------------

-  54-arphandler.xml

   -  is-proactive-flood-mode

      -  "true" means that flood flows will be installed on each switch.
         With this flood flow, each switch will flood a packet that
         doesn’t match any other flows.

         -  Advantage: Fewer packets are sent to the controller because
            those packets are flooded to the network.

         -  Disadvantage: A lot of network traffic is generated.

      -  "false" means the previously mentioned flood flows will not be
         installed. Instead an ARP flow will be installed on each switch
         that sends all ARP packets to the controller.

         -  Advantage: Less network traffic is generated.

         -  Disadvantage: The controller handles more packets (ARP
            requests & replies) and the ARP process takes longer than if
            there were flood flows.

   -  flood-flow-table-id

      -  The flood flow will be installed on the specified flow table of
         each switch

      -  This field is only relevant when "is-proactive-flood-mode" is
         set to "true"

   -  flood-flow-priority

      -  The flood flow will be installed with the specified priority

      -  This field is only relevant when "is-proactive-flood-mode" is
         set to "true"

   -  flood-flow-idle-timeout

      -  The flood flow will timeout (removed from the switch) if the
         flow doesn’t forward a packet for *x* seconds

      -  This field is only relevant when "is-proactive-flood-mode" is
         set to "true"

   -  flood-flow-hard-timeout

      -  The flood flow will timeout (removed from the switch) after *x*
         seconds, regardless of how many packets it is forwarding

      -  This field is only relevant when "is-proactive-flood-mode" is
         set to "true"

   -  arp-flow-table-id

      -  The ARP flow will be installed on the specified flow table of
         each switch

      -  This field is only relevant when "is-proactive-flood-mode" is
         set to "false"

   -  arp-flow-priority

      -  The ARP flow will be installed with the specified priority

      -  This field is only relevant when "is-proactive-flood-mode" is
         set to "false"

   -  arp-flow-idle-timeout

      -  The ARP flow will timeout (removed from the switch) if the flow
         doesn’t forward a packet for *x* seconds

      -  This field is only relevant when "is-proactive-flood-mode" is
         set to "false"

   -  arp-flow-hard-timeout

      -  The ARP flow will timeout (removed from the switch) after
         *arp-flow-hard-timeout* seconds, regardless of how many packets
         it is forwarding

      -  This field is only relevant when "is-proactive-flood-mode" is
         set to "false"

Configuring Address Tracker
---------------------------

-  56-addresstracker.xml

   -  timestamp-update-interval

      -  A last-seen timestamp is associated with each address. This
         last-seen timestamp will only be updated after
         *timestamp-update-interval* milliseconds.

      -  A higher value has the advantage of performing less writes to
         the database.

      -  A lower value has the advantage of knowing how fresh an address
         is.

   -  observe-addresses-from

      -  IP and MAC addresses can be observed/learned from ARP, IPv4,
         and IPv6 packets. Set which packets to make these observations
         from.

Configuring L2Switch Main
-------------------------

-  58-l2switchmain.xml

   -  is-install-dropall-flow

      -  "true" means a drop-all flow will be installed on each switch,
         so the default action will be to drop a packet instead of
         sending it to the controller

      -  "false" means this flow will not be installed

   -  dropall-flow-table-id

      -  The dropall flow will be installed on the specified flow table
         of each switch

      -  This field is only relevant when "is-install-dropall-flow" is
         set to "true"

   -  dropall-flow-priority

      -  The dropall flow will be installed with the specified priority

      -  This field is only relevant when "is-install-dropall-flow" is
         set to "true"

   -  dropall-flow-idle-timeout

      -  The dropall flow will timeout (removed from the switch) if the
         flow doesn’t forward a packet for *x* seconds

      -  This field is only relevant when "is-install-dropall-flow" is
         set to "true"

   -  dropall-flow-hard-timeout

      -  The dropall flow will timeout (removed from the switch) after
         *x* seconds, regardless of how many packets it is forwarding

      -  This field is only relevant when "is-install-dropall-flow" is
         set to "true"

   -  is-learning-only-mode

      -  "true" means that the L2Switch will only be learning addresses.
         No additional flows to optimize network traffic will be
         installed.

      -  "false" means that the L2Switch will react to network traffic
         and install flows on the switches to optimize traffic.
         Currently, MAC-to-MAC flows are installed.

   -  reactive-flow-table-id

      -  The reactive flow will be installed on the specified flow table
         of each switch

      -  This field is only relevant when "is-learning-only-mode" is set
         to "false"

   -  reactive-flow-priority

      -  The reactive flow will be installed with the specified priority

      -  This field is only relevant when "is-learning-only-mode" is set
         to "false"

   -  reactive-flow-idle-timeout

      -  The reactive flow will timeout (removed from the switch) if the
         flow doesn’t forward a packet for *x* seconds

      -  This field is only relevant when "is-learning-only-mode" is set
         to "false"

   -  reactive-flow-hard-timeout

      -  The reactive flow will timeout (removed from the switch) after
         *x* seconds, regardless of how many packets it is forwarding

      -  This field is only relevant when "is-learning-only-mode" is set
         to "false"

Running the L2Switch project
----------------------------

To run the L2 Switch inside the Lithium OpenDaylight distribution simply
install the ``odl-l2switch-switch-ui`` feature;

::

    feature:install odl-l2switch-switch-ui

Create a network using mininet
------------------------------

::

    sudo mn --controller=remote,ip=<Controller IP> --topo=linear,3 --switch ovsk,protocols=OpenFlow13
    sudo mn --controller=remote,ip=127.0.0.1 --topo=linear,3 --switch ovsk,protocols=OpenFlow13

The above command will create a virtual network consisting of 3
switches. Each switch will connect to the controller located at the
specified IP, i.e. 127.0.0.1

::

    sudo mn --controller=remote,ip=127.0.0.1 --mac --topo=linear,3 --switch ovsk,protocols=OpenFlow13

The above command has the "mac" option, which makes it easier to
distinguish between Host MAC addresses and Switch MAC addresses.

Generating network traffic using mininet
----------------------------------------

::

    h1 ping h2

The above command will cause host1 (h1) to ping host2 (h2)

::

    pingall

*pingall* will cause each host to ping every other host.

Checking Address Observations
-----------------------------

Address Observations are added to the Inventory data tree.

The Address Observations on a Node Connector can be checked through a
browser or a REST Client.

::

    http://10.194.126.91:8080/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/node-connector/openflow:1:1

.. figure:: ./images/l2switch-address-observations.png
   :alt: Address Observations

   Address Observations

Checking Hosts
--------------

Host information is added to the Topology data tree.

-  Host address

-  Attachment point (link) to a node/switch

This host information and attachment point information can be checked
through a browser or a REST Client.

::

    http://10.194.126.91:8080/restconf/operational/network-topology:network-topology/topology/flow:1/

.. figure:: ./images/l2switch-hosts.png
   :alt: Hosts

   Hosts

Checking STP status of each link
--------------------------------

STP Status information is added to the Inventory data tree.

-  A status of "forwarding" means the link is active and packets are
   flowing on it.

-  A status of "discarding" means the link is inactive and packets are
   not sent over it.

The STP status of a link can be checked through a browser or a REST
Client.

::

    http://10.194.126.91:8080/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/node-connector/openflow:1:2

.. figure:: ./images/l2switch-stp-status.png
   :alt: STP status

   STP status

Miscellaneous mininet commands
------------------------------

::

    link s1 s2 down

This will bring the link between switch1 (s1) and switch2 (s2) down

::

    link s1 s2 up

This will bring the link between switch1 (s1) and switch2 (s2) up

::

    link s1 h1 down

This will bring the link between switch1 (s1) and host1 (h1) down

L3VPN Service: User Guide
=========================

Overview
--------

L3VPN Service in OpenDaylight provides a framework to create L3VPN based
on BGP-MP. It also helps to create Network Virtualization for DC Cloud
environment.

Modules & Interfaces
--------------------

L3VPN service can be realized using the following modules -

VPN Service Modules
~~~~~~~~~~~~~~~~~~~

1. **VPN Manager** : Creates and manages VPNs and VPN Interfaces

2. **BGP Manager** : Configures BGP routing stack and provides interface
   to routing services

3. **FIB Manager** : Provides interface to FIB, creates and manages
   forwarding rules in Dataplane

4. **Nexthop Manager** : Creates and manages nexthop egress pointer,
   creates egress rules in Dataplane

5. **Interface Manager** : Creates and manages different type of network
   interfaces, e.g., VLAN, l3tunnel etc.,

6. **Id Manager** : Provides cluster-wide unique ID for a given key.
   Used by different modules to get unique IDs for different entities.

7. **MD-SAL Util** : Provides interface to MD-SAL. Used by service
   modules to access MD-SAL Datastore and services.

All the above modules can function independently and can be utilized by
other services as well.

Configuration Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~

The following modules expose configuration interfaces through which user
can configure L3VPN Service.

1. BGP Manager

2. VPN Manager

3. Interface Manager

4. FIB Manager

Configuration Interface Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Data Node Path : */config/bgp:bgp-router/*

   a. Fields :

      i.  local-as-identifier

      ii. local-as-number

   b. REST Methods : GET, PUT, DELETE, POST

2. Data Node Path : */config/bgp:bgp-neighbors/*

   a. Fields :

      i. List of bgp-neighbor

   b. REST Methods : GET, PUT, DELETE, POST

3. Data Node Path :
   */config/bgp:bgp-neighbors/bgp-neighbor/``{as-number}``/*

   a. Fields :

      i.  as-number

      ii. ip-address

   b. REST Methods : GET, PUT, DELETE, POST

1. Data Node Path : */config/l3vpn:vpn-instances/*

   a. Fields :

      i. List of vpn-instance

   b. REST Methods : GET, PUT, DELETE, POST

2. Data Node Path : */config/l3vpn:vpn-interfaces/vpn-instance*

   a. Fields :

      i.   name

      ii.  route-distinguisher

      iii. import-route-policy

      iv.  export-route-policy

   b. REST Methods : GET, PUT, DELETE, POST

3. Data Node Path : */config/l3vpn:vpn-interfaces/*

   a. Fields :

      i. List of vpn-interface

   b. REST Methods : GET, PUT, DELETE, POST

4. Data Node Path : */config/l3vpn:vpn-interfaces/vpn-interface*

   a. Fields :

      i.  name

      ii. vpn-instance-name

   b. REST Methods : GET, PUT, DELETE, POST

5. Data Node Path :
   */config/l3vpn:vpn-interfaces/vpn-interface/``{name}``/adjacency*

   a. Fields :

      i.  ip-address

      ii. mac-address

   b. REST Methods : GET, PUT, DELETE, POST

1. Data Node Path : */config/if:interfaces/interface*

   a. Fields :

      i.   name

      ii.  type

      iii. enabled

      iv.  of-port-id

      v.   tenant-id

      vi.  base-interface

   b. type specific fields

      i.   when type = *l2vlan*

           A. vlan-id

      ii.  when type = *stacked\_vlan*

           A. stacked-vlan-id

      iii. when type = *l3tunnel*

           A. tunnel-type

           B. local-ip

           C. remote-ip

           D. gateway-ip

      iv.  when type = *mpls*

           A. list labelStack

           B. num-labels

   c. REST Methods : GET, PUT, DELETE, POST

1. Data Node Path : */config/odl-fib:fibEntries/vrfTables*

   a. Fields :

      i. List of vrfTables

   b. REST Methods : GET, PUT, DELETE, POST

2. Data Node Path :
   */config/odl-fib:fibEntries/vrfTables/``{routeDistinguisher}``/*

   a. Fields :

      i.  route-distinguisher

      ii. list vrfEntries

          A. destPrefix

          B. label

          C. nexthopAddress

   b. REST Methods : GET, PUT, DELETE, POST

3. Data Node Path : */config/odl-fib:fibEntries/ipv4Table*

   a. Fields :

      i. list ipv4Entry

         A. destPrefix

         B. nexthopAddress

   b. REST Methods : GET, PUT, DELETE, POST

Provisioning Sequence & Sample Configurations
---------------------------------------------

Installation
~~~~~~~~~~~~

1. Edit *etc/custom.properties* and set the following property:
   *vpnservice.bgpspeaker.host.name = <bgpserver-ip>* *<bgpserver-ip>*
   here refers to the IP address of the host where BGP is running.

2. Run ODL and install VPN Service *feature:install odl-vpnservice-core*

Use REST interface to configure L3VPN service

Pre-requisites:
~~~~~~~~~~~~~~~

1. BGP stack with VRF support needs to installed and configured

   a. *Configure BGP as specified in Step 1 below.*

2. Create pairs of GRE/VxLAN Tunnels (using ovsdb/ovs-vsctl) between
   each switch and between each switch to the Gateway node

   a. *Create *l3tunnel* interfaces corresponding to each tunnel in
      interfaces DS as specified in Step 2 below.*

Step 1 : Configure BGP
~~~~~~~~~~~~~~~~~~~~~~

1. Configure BGP Router
^^^^^^^^^^^^^^^^^^^^^^^

**REST API** : *PUT /config/bgp:bgp-router/*

**Sample JSON Data**

.. code:: json

    {
        "bgp-router": {
            "local-as-identifier": "10.10.10.10",
            "local-as-number": 108
        }
    }

2. Configure BGP Neighbors
^^^^^^^^^^^^^^^^^^^^^^^^^^

**REST API** : *PUT /config/bgp:bgp-neighbors/*

**Sample JSON Data**

.. code:: json

      {
         "bgp-neighbor" : [
                {
                    "as-number": 105,
                    "ip-address": "169.144.42.168"
                }
           ]
       }

Step 2 : Create Tunnel Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create l3tunnel interfaces corresponding to all GRE/VxLAN tunnels
created with ovsdb (`refer Prerequisites <#prer>`__). Use following REST
Interface -

**REST API** : *PUT /config/if:interfaces/if:interfacce*

**Sample JSON Data**

.. code:: json

    {
        "interface": [
            {
                "name" : "GRE_192.168.57.101_192.168.57.102",
                "type" : "odl-interface:l3tunnel",
                "odl-interface:tunnel-type": "odl-interface:tunnel-type-gre",
                "odl-interface:local-ip" : "192.168.57.101",
                "odl-interface:remote-ip" : "192.168.57.102",
                "odl-interface:portId" : "openflow:1:3",
                "enabled" : "true"
            }
        ]
    }

Following is expected as a result of these configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Unique If-index is generated

2. *Interface-state* operational DS is updated

3. Corresponding Nexthop Group Entry is created

Step 3 : OS Create Neutron Ports and attach VMs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At this step user creates VMs.

Step 4 : Create VM Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create l2vlan interfaces corresponding to VM created in step 3

**REST API** : *PUT /config/if:interfaces/if:interface*

**Sample JSON Data**

.. code:: json

    {
        "interface": [
            {
                "name" : "dpn1-dp1.2",
                "type" : "l2vlan",
                "odl-interface:of-port-id" : "openflow:1:2",
                "odl-interface:vlan-id" : "1",
                "enabled" : "true"
            }
        ]
    }

Step 5: Create VPN Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**REST API** : *PUT /config/l3vpn:vpn-instances/l3vpn:vpn-instance/*

**Sample JSON Data**

.. code:: json

    {
      "vpn-instance": [
        {
            "description": "Test VPN Instance 1",
            "vpn-instance-name": "testVpn1",
            "ipv4-family": {
                "route-distinguisher": "4000:1",
                "export-route-policy": "4000:1,5000:1",
                "import-route-policy": "4000:1,5000:1",
            }
        }
      ]
    }

Following is expected as a result of these configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. VPN ID is allocated and updated in data-store

2. Corresponding VRF is created in BGP

3. If there are vpn-interface configurations for this VPN, corresponding
   action is taken as defined in step 5

Step 5 : Create VPN-Interface and Local Adjacency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*this can be done in two steps as well*

1. Create vpn-interface
^^^^^^^^^^^^^^^^^^^^^^^

**REST API** : *PUT /config/l3vpn:vpn-interfaces/l3vpn:vpn-interface/*

**Sample JSON Data**

.. code:: json

    {
      "vpn-interface": [
        {
          "vpn-instance-name": "testVpn1",
          "name": "dpn1-dp1.2",
        }
      ]
    }

    **Note**

    name here is the name of VM interface created in step 3, 4

2. Add Adjacencies on vpn-interafce
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**REST API** : *PUT
/config/l3vpn:vpn-interfaces/l3vpn:vpn-interface/dpn1-dp1.3/adjacency*

**Sample JSON Data**

.. code:: json

      {
         "adjacency" : [
                {
                    "ip-address" : "169.144.42.168",
                    "mac-address" : "11:22:33:44:55:66"
                }
           ]
       }

    its a list, user can define more than one adjacency on a
    vpn\_interface

Above steps can be carried out in a single step as following

.. code:: json

    {
        "vpn-interface": [
            {
                "vpn-instance-name": "testVpn1",
                "name": "dpn1-dp1.3",
                "odl-l3vpn:adjacency": [
                    {
                        "odl-l3vpn:mac_address": "11:22:33:44:55:66",
                        "odl-l3vpn:ip_address": "11.11.11.2",
                    }
                ]
            }
        ]
    }

Following is expected as a result of these configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Prefix label is generated and stored in DS

2. Ingress table is programmed with flow corresponding to interface

3. Local Egress Group is created

4. Prefix is added to BGP for advertisement

5. BGP pushes route update to FIB YANG Interface

6. FIB Entry flow is added to FIB Table in OF pipeline

Link Aggregation Control Protocol User Guide
============================================

Overview
--------

This section contains information about how to use the LACP plugin
project with OpenDaylight, including configurations.

Link Aggregation Control Protocol Architecture
----------------------------------------------

The LACP Project within OpenDaylight implements Link Aggregation Control
Protocol (LACP) as an MD-SAL service module and will be used to
auto-discover and aggregate multiple links between an OpenDaylight
controlled network and LACP-enabled endpoints or switches. The result is
the creation of a logical channel, which represents the aggregation of
the links. Link aggregation provides link resiliency and bandwidth
aggregation. This implementation adheres to IEEE Ethernet specification
`802.3ad <http://www.ieee802.org/3/hssg/public/apr07/frazier_01_0407.pdf>`__.

Configuring Link Aggregation Control Protocol
---------------------------------------------

This feature can be enabled in the Karaf console of the OpenDaylight
Karaf distribution by issuing the following command:

::

    feature:install odl-lacp-ui

    **Note**

    1. Ensure that legacy (non-OpenFlow) switches are configured with
       LACP mode active with a long timeout to allow for the LACP plugin
       in OpenDaylight to respond to its messages.

    2. Flows that want to take advantage of LACP-configured Link
       Aggregation Groups (LAGs) must explicitly use a OpenFlow group
       table entry created by the LACP plugin. The plugin only creates
       group table entries, it does not program any flows on its own.

Administering or Managing Link Aggregation Control Protocol
-----------------------------------------------------------

LACP-discovered network inventory and network statistics can be viewed
using the following REST APIs.

1. List of aggregators available for a node:

   ::

       http://<ControllerIP>:8181/restconf/operational/opendaylight-inventory:nodes/node/<node-id>

   Aggregator information will appear within the ``<lacp-aggregators>``
   XML tag.

2. To view only the information of an aggregator:

   ::

       http://<ControllerIP>:8181/restconf/operational/opendaylight-inventory:nodes/node/<node-id>/lacp-aggregators/<agg-id>

   The group ID associated with the aggregator can be found inside the
   ``<lag-groupid>`` XML tag.

   The group table entry information for the ``<lag-groupid>`` added for
   the aggregator is also available in the ``opendaylight-inventory``
   node database.

3. To view physical port information.

   ::

       http://<ControllerIP>:8181/restconf/operational/opendaylight-inventory:nodes/node/<node-id>/node-connector/<node-connector-id>

   Ports that are associated with an aggregator will have the tag
   ``<lacp-agg-ref>`` updated with valid aggregator information.

Tutorials
---------

The below tutorial demonstrates LACP LAG creation for a sample mininet
topology.

Sample LACP Topology creation on Mininet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    sudo mn --controller=remote,ip=<Controller IP> --topo=linear,1 --switch ovsk,protocols=OpenFlow13

The above command will create a virtual network consisting of a switch
and a host. The switch will be connected to the controller.

Once the topology is discovered, verify the presence of a flow entry
with "dl\_type" set to "0x8809" to handle LACP packets using the below
ovs-ofctl command:

::

    ovs-ofctl -O OpenFlow13 dump-flows s1
     OFPST_FLOW reply (OF1.3) (xid=0x2):
     cookie=0x300000000000001e, duration=60.067s, table=0, n_packets=0, n_bytes=0, priority=5,dl_dst=01:80:c2:00:00:02,dl_type=0x8809 actions=CONTROLLER:65535

Configure an additional link between the switch (s1) and host (h1) using
the below command on mininet shell to aggregate 2 links:

::

    mininet> py net.addLink(s1, net.get('h1'))
    mininet> py s1.attach('s1-eth2')

The LACP module will listen for LACP control packets that are generated
from legacy switch (non-OpenFlow enabled). In our example, host (h1)
will act as a LACP packet generator. In order to generate the LACP
control packets, a bond interface has to be created on the host (h1)
with mode type set to LACP with long-timeout. To configure bond
interface, create a new file bonding.conf under the /etc/modprobe.d/
directory and insert the below lines in this new file:

::

    alias bond0 bonding
    options bonding mode=4

Here mode=4 is referred to LACP and the default timeout is set to long.

Enable bond interface and associate both physical interface h1-eth0 &
h1-eth1 as members of the bond interface on host (h1) using the below
commands on the mininet shell:

::

    mininet> py net.get('h1').cmd('modprobe bonding')
    mininet> py net.get('h1').cmd('ip link add bond0 type bond')
    mininet> py net.get('h1').cmd('ip link set bond0 address <bond-mac-address>')
    mininet> py net.get('h1').cmd('ip link set h1-eth0 down')
    mininet> py net.get('h1').cmd('ip link set h1-eth0 master bond0')
    mininet> py net.get('h1').cmd('ip link set h1-eth1 down')
    mininet> py net.get('h1').cmd('ip link set h1-eth1 master bond0')
    mininet> py net.get('h1').cmd('ip link set bond0 up')

Once the bond0 interface is up, the host (h1) will send LACP packets to
the switch (s1). The LACP Module will then create a LAG through exchange
of LACP packets between the host (h1) and switch (s1). To view the bond
interface output on the host (h1) side:

::

    mininet> py net.get('h1').cmd('cat /proc/net/bonding/bond0')
    Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011)
    Bonding Mode: IEEE 802.3ad Dynamic link aggregation
    Transmit Hash Policy: layer2 (0)
    MII Status: up
    MII Polling Interval (ms): 100
    Up Delay (ms): 0
    Down Delay (ms): 0
    802.3ad info
    LACP rate: slow
    Min links: 0
    Aggregator selection policy (ad_select): stable
    Active Aggregator Info:
            Aggregator ID: 1
            Number of ports: 2
            Actor Key: 33
            Partner Key: 27
            Partner Mac Address: 00:00:00:00:01:01

::

    Slave Interface: h1-eth0
    MII Status: up
    Speed: 10000 Mbps
    Duplex: full
    Link Failure Count: 0
    Permanent HW addr: 00:00:00:00:00:11
    Aggregator ID: 1
    Slave queue ID: 0

::

    Slave Interface: h1-eth1
    MII Status: up
    Speed: 10000 Mbps
    Duplex: full
    Link Failure Count: 0
    Permanent HW addr: 00:00:00:00:00:12
    Aggregator ID: 1
    Slave queue ID: 0

A corresponding group table entry would be created on the OpenFlow
switch (s1) with "type" set to "select" to perform the LAG
functionality. To view the group entries:

::

    mininet>ovs-ofctl -O Openflow13 dump-groups s1
    OFPST_GROUP_DESC reply (OF1.3) (xid=0x2):
     group_id=60169,type=select,bucket=weight:0,actions=output:1,output:2

To apply the LAG functionality on the switches, the flows should be
configured with action set to GroupId instead of output port. A sample
add-flow configuration with output action set to GroupId:

::

    sudo ovs-ofctl -O Openflow13 add-flow s1 dl_type=0x0806,dl_src=SRC_MAC,dl_dst=DST_MAC,actions=group:60169

LISP Flow Mapping User Guide
============================

Overview
--------

Locator/ID Separation Protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Locator/ID Separation Protocol
(LISP) <http://tools.ietf.org/html/rfc6830>`__ is a technology that
provides a flexible map-and-encap framework that can be used for overlay
network applications such as data center network virtualization and
Network Function Virtualization (NFV).

LISP provides the following name spaces:

-  `Endpoint Identifiers
   (EIDs) <http://tools.ietf.org/html/rfc6830#page-6>`__

-  `Routing Locators
   (RLOCs) <http://tools.ietf.org/html/rfc6830#section-3>`__

In a virtualization environment EIDs can be viewed as virtual address
space and RLOCs can be viewed as physical network address space.

The LISP framework decouples network control plane from the forwarding
plane by providing:

-  A data plane that specifies how the virtualized network addresses are
   encapsulated in addresses from the underlying physical network.

-  A control plane that stores the mapping of the virtual-to-physical
   address spaces, the associated forwarding policies and serves this
   information to the data plane on demand.

Network programmability is achieved by programming forwarding policies
such as transparent mobility, service chaining, and traffic engineering
in the mapping system; where the data plane elements can fetch these
policies on demand as new flows arrive. This chapter describes the LISP
Flow Mapping project in OpenDaylight and how it can be used to enable
advanced SDN and NFV use cases.

LISP data plane Tunnel Routers are available at
`LISPmob.org <http://LISPmob.org/>`__ in the open source community on
the following platforms:

-  Linux

-  Android

-  OpenWRT

For more details and support for LISP data plane software please visit
`the LISPmob web site <http://LISPmob.org/>`__.

LISP Flow Mapping Service
~~~~~~~~~~~~~~~~~~~~~~~~~

The LISP Flow Mapping service provides LISP Mapping System services.
This includes LISP Map-Server and LISP Map-Resolver services to store
and serve mapping data to data plane nodes as well as to OpenDaylight
applications. Mapping data can include mapping of virtual addresses to
physical network address where the virtual nodes are reachable or hosted
at. Mapping data can also include a variety of routing policies
including traffic engineering and load balancing. To leverage this
service, OpenDaylight applications and services can use the northbound
REST API to define the mappings and policies in the LISP Mapping
Service. Data plane devices capable of LISP control protocol can
leverage this service through a southbound LISP plugin. LISP-enabled
devices must be configured to use this OpenDaylight service as their Map
Server and/or Map Resolver.

The southbound LISP plugin supports the LISP control protocol
(Map-Register, Map-Request, Map-Reply messages), and can also be used to
register mappings in the OpenDaylight mapping service.

LISP Flow Mapping Architecture
------------------------------

The following figure shows the various LISP Flow Mapping modules.

.. figure:: ./images/ODL_lfm_Be_component.jpg
   :alt: LISP Mapping Service Internal Architecture

   LISP Mapping Service Internal Architecture

A brief description of each module is as follows:

-  **DAO (Data Access Object):** This layer separates the LISP logic
   from the database, so that we can separate the map server and map
   resolver from the specific implementation of the mapping database.
   Currently we have an implementation of this layer with an in-memory
   HashMap, but it can be switched to any other key/value store and you
   only need to implement the ILispDAO interface.

-  **Map Server:** This module processes the adding or registration of
   authentication tokens (keys) and mappings. For a detailed
   specification of LISP Map Server, see
   `LISP <http://tools.ietf.org/search/rfc6830>`__.

-  **Map Resolver:** This module receives and processes the mapping
   lookup queries and provides the mappings to requester. For a detailed
   specification of LISP Map Server, see
   `LISP <http://tools.ietf.org/search/rfc6830>`__.

-  **RPC/RESTCONF:** This is the auto-generated RESTCONF-based
   northbound API. This module enables defining key-EID associations as
   well as adding mapping information through the Map Server. Key-EID
   associations and mappings can also be queried via this API.

-  **GUI:** This module enables adding and querying the mapping service
   through a GUI based on ODL DLUX.

-  **Neutron:** This module implements the OpenDaylight Neutron Service
   APIs. It provides integration between the LISP service and the
   OpenDaylight Neutron service, and thus OpenStack.

-  **Java API:** The API module exposes the Map Server and Map Resolver
   capabilities via a Java API.

-  **LISP Proto:** This module includes LISP protocol dependent data
   types and associated processing.

-  **In Memory DB:** This module includes the in memory database
   implementation of the mapping service.

-  **LISP Southbound Plugin:** This plugin enables data plane devices
   that support LISP control plane protocol (see
   `LISP <http://tools.ietf.org/search/rfc6830>`__) to register and
   query mappings to the LISP Flow Mapping via the LISP control plane
   protocol.

Configuring LISP Flow Mapping
-----------------------------

In order to use the LISP mapping service for registering EID to RLOC
mappings from northbound or southbound, keys have to be defined for the
EID prefixes first. Once a key is defined for an EID prefix, it can be
used to add mappings for that EID prefix multiple times. If the service
is going to be used to process Map-Register messages from the southbound
LISP plugin, the same key must be used by the data plane device to
create the authentication data in the Map-Register messages for the
associated EID prefix.

The ``etc/custom.properties`` file in the Karaf distribution allows
configuration of several OpenDaylight parameters. The LISP service has
the following properties that can be adjusted:

**lisp.mappingOverwrite** (default: *true*)
    Configures handling of mapping updates. When set to *true* (default)
    a mapping update (either through the southbound plugin via a
    Map-Register message or through a northbound API PUT REST call) the
    existing RLOC set associated to an EID prefix is overwritten. When
    set to *false*, the RLOCs of the update are merged to the existing
    set.

**lisp.smr** (default: *false*)
    Enables/disables the `Solicit-Map-Request
    (SMR) <http://tools.ietf.org/html/rfc6830#section-6.6.2>`__
    functionality. SMR is a method to notify changes in an EID-to-RLOC
    mapping to "subscribers". The LISP service considers all
    Map-Request’s source RLOC as a subscriber to the requested EID
    prefix, and will send an SMR control message to that RLOC if the
    mapping changes.

**lisp.elpPolicy** (default: *default*)
    Configures how to build a Map-Reply southbound message from a
    mapping containing an Explicit Locator Path (ELP) RLOC. It is used
    for compatibility with dataplane devices that don’t understand the
    ELP LCAF format. The *default* setting doesn’t alter the mapping,
    returning all RLOCs unmodified. The *both* setting adds a new RLOC
    to the mapping, with a lower priority than the ELP, that is the next
    hop in the service chain. To determine the next hop, it searches the
    source RLOC of the Map-Request in the ELP, and chooses the next hop,
    if it exists, otherwise it chooses the first hop. The *replace*
    setting adds a new RLOC using the same algorithm as the *both*
    setting, but using the origin priority of the ELP RLOC, which is
    removed from the mapping.

**lisp.lookupPolicy** (default: *northboundFirst*)
    Configures the mapping lookup algorithm. When set to
    *northboundFirst* mappings programmed through the northbound API
    will take precedence. If no northbound programmed mappings exist,
    then the mapping service will return mappings registered through the
    southbound plugin, if any exists. When set to
    *northboundAndSouthbound* the mapping programmed by the northbound
    is returned, updated by the up/down status of these mappings as
    reported by the southbound (if existing).

**lisp.mappingMerge** (default: *false*)
    Configures the merge policy on the southbound registrations through
    the LISP SB Plugin. When set to *false*, only the latest mapping
    registered through the SB plugin is valid in the southbound mapping
    database, independent of which device it came from. When set to
    *true*, mappings for the same EID registered by different devices
    are merged together and a union of the locators is maintained as the
    valid mapping for that EID.

Textual Conventions for LISP Address Formats
--------------------------------------------

In addition to the more common IPv4, IPv6 and MAC address data types,
the LISP control plane supports arbitrary `Address Family
Identifiers <http://www.iana.org/assignments/address-family-numbers>`__
assigned by IANA, and in addition to those the `LISP Canoncal Address
Format (LCAF) <https://tools.ietf.org/html/draft-ietf-lisp-lcaf>`__.

The LISP Flow Mapping project in OpenDaylight implements support for
many of these different address formats, the full list being summarized
in the following table. While some of the address formats have well
defined and widely used textual representation, many don’t. It became
necessary to define a convention to use for text rendering of all
implemented address types in logs, URLs, input fields, etc. The below
table lists the supported formats, along with their AFI number and LCAF
type, including the prefix used for disambiguation of potential overlap,
and examples output.

+------------------+----------+----------+----------+----------------------------------+
| Name             | AFI      | LCAF     | Prefix   | Text Rendering                   |
+==================+==========+==========+==========+==================================+
| **No Address**   | 0        | -        | no:      | No Address Present               |
+------------------+----------+----------+----------+----------------------------------+
| **IPv4 Prefix**  | 1        | -        | ipv4:    | 192.0.2.0/24                     |
+------------------+----------+----------+----------+----------------------------------+
| **IPv6 Prefix**  | 2        | -        | ipv6:    | 2001:db8::/32                    |
+------------------+----------+----------+----------+----------------------------------+
| **MAC Address**  | 16389    | -        | mac:     | 00:00:5E:00:53:00                |
+------------------+----------+----------+----------+----------------------------------+
| **Distinguished  | 17       | -        | dn:      | stringAsIs                       |
| Name**           |          |          |          |                                  |
+------------------+----------+----------+----------+----------------------------------+
| **AS Number**    | 18       | -        | as:      | AS64500                          |
+------------------+----------+----------+----------+----------------------------------+
| **AFI List**     | 16387    | 1        | list:    | {192.0.2.1,192.0.2.2,2001:db8::1 |
|                  |          |          |          | }                                |
+------------------+----------+----------+----------+----------------------------------+
| **Instance ID**  | 16387    | 2        | -        | [223] 192.0.2.0/24               |
+------------------+----------+----------+----------+----------------------------------+
| **Application    | 16387    | 4        | appdata: | 192.0.2.1!128!17!80-81!6667-7000 |
| Data**           |          |          |          |                                  |
+------------------+----------+----------+----------+----------------------------------+
| **Explicit       | 16387    | 10       | elp:     | {192.0.2.1→192.0.2.2\|lps→192.0. |
| Locator Path**   |          |          |          | 2.3}                             |
+------------------+----------+----------+----------+----------------------------------+
| **Source/Destina | 16387    | 12       | srcdst:  | 192.0.2.1/32\|192.0.2.2/32       |
| tion             |          |          |          |                                  |
| Key**            |          |          |          |                                  |
+------------------+----------+----------+----------+----------------------------------+
| **Key/Value      | 16387    | 15       | kv:      | 192.0.2.1⇒192.0.2.2              |
| Address Pair**   |          |          |          |                                  |
+------------------+----------+----------+----------+----------------------------------+
| **Service Path** | 16387    | N/A      | sp:      | 42(3)                            |
+------------------+----------+----------+----------+----------------------------------+

Table: LISP Address Formats

Please note that the forward slash character ``/`` typically separating
IPv4 and IPv6 addresses from the mask length is transformed into ``%2f``
when used in a URL.

Karaf commands
--------------

In this section we will discuss two types of Karaf commands: built-in,
and LISP specific. Some built-in commands are quite useful, and are
needed for the tutorial, so they will be discussed here. A reference of
all LISP specific commands, added by the LISP Flow Mapping project is
also included. They are useful mostly for debugging.

Useful built-in commands
~~~~~~~~~~~~~~~~~~~~~~~~

``help``
    Lists all available command, with a short description of each.

``help <command_name>``
    Show detailed help about a specific command.

``feature:list [-i]``
    Show all locally available features in the Karaf container. The
    ``-i`` option lists only features that are currently installed. It
    is possible to use ``| grep`` to filter the output (for all
    commands, not just this one).

``feature:install <feature_name>``
    Install feature ``feature_name``.

``log:set <level> <class>``
    Set the log level for ``class`` to ``level``. The default log level
    for all classes is INFO. For debugging, or learning about LISP
    internals it is useful to run
    ``log:set TRACE org.opendaylight.lispflowmapping`` right after Karaf
    starts up.

``log:display``
    Outputs the log file to the console, and returns control to the
    user.

``log:tail``
    Continuously shows log output, requires ``Ctrl+C`` to return to the
    console.

LISP specific commands
~~~~~~~~~~~~~~~~~~~~~~

The available lisp commands can always be obtained by
``help mappingservice``. Currently they are:

``mappingservice:addkey``
    Add the default password ``password`` for the IPv4 EID prefix
    0.0.0.0/0 (all addresses). This is useful when experimenting with
    southbound devices, and using the REST interface would be combersome
    for whatever reason.

``mappingservice:mappings``
    Show the list of all mappings stored in the internal non-persistent
    data store (the DAO), listing the full data structure. The output is
    not human friendly, but can be used for debugging.

LISP Flow Mapping Karaf Features
--------------------------------

LISP Flow Mapping has the following Karaf features that can be installed
from the Karaf console:

``odl-lispflowmapping-msmr``
    This includes the core features required to use the LISP Flow
    Mapping Service such as mapping service and the LISP southbound
    plugin.

``odl-lispflowmapping-ui``
    This includes the GUI module for the LISP Mapping Service.

``odl-lispflowmapping-neutron``
    This is the experimental Neutron provider module for LISP mapping
    service.

Tutorials
---------

This section provides a tutorial demonstrating various features in this
service.

Creating a LISP overlay
~~~~~~~~~~~~~~~~~~~~~~~

This section provides instructions to set up a LISP network of three
nodes (one "client" node and two "server" nodes) using LISPmob as data
plane LISP nodes and the LISP Flow Mapping project from OpenDaylight as
the LISP programmable mapping system for the LISP network.

Overview
^^^^^^^^

The steps shown below will demonstrate setting up a LISP network between
a client and two servers, then performing a failover between the two
"server" nodes.

Prerequisites
^^^^^^^^^^^^^

-  **OpenDaylight Beryllium**

-  **The Postman Chrome App**: the most convenient way to follow along
   this tutorial is to use the `Postman Chrome
   App <https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en>`__
   to edit and send the requests. The project git repository hosts a
   collection of the requests that are used in this tutorial in the
   ``resources/tutorial/Beryllium_Tutorial.json.postman_collection``
   file. You can import this file to Postman by clicking *Import* at the
   top, choosing *Download from link* and then entering the following
   URL:
   ``https://git.opendaylight.org/gerrit/gitweb?p=lispflowmapping.git;a=blob_plain;f=resources/tutorial/Beryllium_Tutorial.json.postman_collection;hb=refs/heads/stable/beryllium``.
   Alternatively, you can save the file on your machine, or if you have
   the repository checked out, you can import from there. You will need
   to create a new Postman Environment and define some variables within:
   ``controllerHost`` set to the hostname or IP address of the machine
   running the ODL instance, and ``restconfPort`` to 8181, if you didn’t
   modify the default controller settings.

-  **LISPmob version 0.5.x** The README.md lists the dependencies needed
   to build it from source.

-  **A virtualization platform**

Target Environment
^^^^^^^^^^^^^^^^^^

The three LISP data plane nodes and the LISP mapping system are assumed
to be running in Linux virtual machines, which have the ``eth0``
interface in NAT mode to allow outside internet access and ``eth1``
connected to a host-only network, with the following IP addresses
(please adjust configuration files, JSON examples, etc. accordingly if
you’re using another addressing scheme):

+--------------------------+--------------------------+--------------------------+
| Node                     | Node Type                | IP Address               |
+==========================+==========================+==========================+
| **controller**           | OpenDaylight             | 192.168.16.11            |
+--------------------------+--------------------------+--------------------------+
| **client**               | LISPmob                  | 192.168.16.30            |
+--------------------------+--------------------------+--------------------------+
| **server1**              | LISPmob                  | 192.168.16.31            |
+--------------------------+--------------------------+--------------------------+
| **server2**              | LISPmob                  | 192.168.16.32            |
+--------------------------+--------------------------+--------------------------+
| **service-node**         | LISPmob                  | 192.168.16.33            |
+--------------------------+--------------------------+--------------------------+

Table: Nodes in the tutorial

    **Note**

    While the tutorial uses LISPmob as the data plane, it could be any
    LISP-enabled hardware or software router (commercial/open source).

Instructions
^^^^^^^^^^^^

The below steps use the command line tool cURL to talk to the LISP Flow
Mapping RPC REST API. This is so that you can see the actual request
URLs and body content on the page.

1.  Install and run OpenDaylight Beryllium release on the controller VM.
    Please follow the general OpenDaylight Beryllium Installation Guide
    for this step. Once the OpenDaylight controller is running install
    the *odl-lispflowmapping-msmr* feature from the Karaf CLI:

    ::

        feature:install odl-lispflowmapping-msmr

    It takes quite a while to load and initialize all features and their
    dependencies. It’s worth running the command ``log:tail`` in the
    Karaf console to see when the log output is winding down, and
    continue with the tutorial after that.

2.  Install LISPmob on the **client**, **server1**, **server2**, and
    **service-node** VMs following the installation instructions `from
    the LISPmob README
    file <https://github.com/LISPmob/lispmob#software-prerequisites>`__.

3.  Configure the LISPmob installations from the previous step. Starting
    from the ``lispd.conf.example`` file in the distribution, set the
    EID in each ``lispd.conf`` file from the IP address space selected
    for your virtual/LISP network. In this tutorial the EID of the
    **client** is set to 1.1.1.1/32, and that of **server1** and
    **server2** to 2.2.2.2/32.

4.  Set the RLOC interface to ``eth1`` in each ``lispd.conf`` file. LISP
    will determine the RLOC (IP address of the corresponding VM) based
    on this interface.

5.  Set the Map-Resolver address to the IP address of the
    **controller**, and on the **client** the Map-Server too. On
    **server1** and **server2** set the Map-Server to something else, so
    that it doesn’t interfere with the mappings on the controller, since
    we’re going to program them manually.

6.  Modify the "key" parameter in each ``lispd.conf`` file to a
    key/password of your choice (*password* in this tutorial).

        **Note**

        The ``resources/tutorial`` directory in the *stable/beryllium*
        branch of the project git repository has the files used in the
        tutorial `checked
        in <https://git.opendaylight.org/gerrit/gitweb?p=lispflowmapping.git;a=tree;f=resources/tutorial;hb=refs/heads/stable/beryllium>`__,
        so you can just copy the files to ``/root/lispd.conf`` on the
        respective VMs. You will also find the JSON files referenced
        below in the same directory.

7.  Define a key and EID prefix association in OpenDaylight using the
    RPC REST API for the **client** EID (1.1.1.1/32) to allow
    registration from the southbound. Since the mappings for the server
    EID will be configured from the REST API, no such association is
    necessary. Run the below command on the **controller** (or any
    machine that can reach **controller**, by replacing *localhost* with
    the IP address of **controller**).

    ::

        curl -u "admin":"admin" -H "Content-type: application/json" -X POST \
            http://localhost:8181/restconf/operations/odl-mappingservice:add-key \
            --data @add-key.json

    where the content of the *add-key.json* file is the following:

    .. code:: json

        {
            "input": {
                "eid": {
                    "address-type": "ietf-lisp-address-types:ipv4-prefix-afi",
                    "ipv4-prefix": "1.1.1.1/32"
                },
                "mapping-authkey": {
                    "key-string": "password",
                    "key-type": 1
                }
            }
        }

8.  Verify that the key is added properly by requesting the following
    URL:

    ::

        curl -u "admin":"admin" -H "Content-type: application/json" -X POST \
            http://localhost:8181/restconf/operations/odl-mappingservice:get-key \
            --data @get1.json

    where the content of the *get1.json* file can be derived from the
    *add-key.json* file by removing the *mapping-authkey* field. The
    output the above invocation should look like this:

    ::

        {"output":{"mapping-authkey":{"key-type":1,"key-string":"password"}}}

9.  Run the ``lispd`` LISPmob daemon on all VMs:

    ::

        lispd -f /root/lispd.conf

10. The **client** LISPmob node should now register its EID-to-RLOC
    mapping in OpenDaylight. To verify you can lookup the corresponding
    EIDs via the REST API

    ::

        curl -u "admin":"admin" -H "Content-type: application/json" -X POST \
            http://localhost:8181/restconf/operations/odl-mappingservice:get-mapping \
            --data @get1.json

    An alternative way for retrieving mappings from ODL using the
    southbound interface is using the
    ```lig`` <https://github.com/davidmeyer/lig>`__ open source tool.

11. Register the EID-to-RLOC mapping of the server EID 2.2.2.2/32 to the
    controller, pointing to **server1** and **server2** with a higher
    priority for **server1**

    ::

        curl -u "admin":"admin" -H "Content-type: application/json" -X POST \
            http://localhost:8181/restconf/operations/odl-mappingservice:add-mapping \
            --data @mapping.json

    where the *mapping.json* file looks like this:

    .. code:: json

        {
            "input": {
                "mapping-record": {
                    "recordTtl": 1440,
                    "action": "NoAction",
                    "authoritative": true,
                    "eid": {
                        "address-type": "ietf-lisp-address-types:ipv4-prefix-afi",
                        "ipv4-prefix": "2.2.2.2/32"
                    },
                    "LocatorRecord": [
                        {
                            "locator-id": "server1",
                            "priority": 1,
                            "weight": 1,
                            "multicastPriority": 255,
                            "multicastWeight": 0,
                            "localLocator": true,
                            "rlocProbed": false,
                            "routed": true,
                            "rloc": {
                                "address-type": "ietf-lisp-address-types:ipv4-afi",
                                "ipv4": "192.168.16.31"
                            }
                        },
                        {
                            "locator-id": "server2",
                            "priority": 2,
                            "weight": 1,
                            "multicastPriority": 255,
                            "multicastWeight": 0,
                            "localLocator": true,
                            "rlocProbed": false,
                            "routed": true,
                            "rloc": {
                                "address-type": "ietf-lisp-address-types:ipv4-afi",
                                "ipv4": "192.168.16.32"
                            }
                        }
                    ]
                }
            }
        }

    Here the priority of the second RLOC (192.168.16.32 - **server2**)
    is 2, a higher numeric value than the priority of 192.168.16.31,
    which is 1. This policy is saying that **server1** is preferred to
    **server2** for reaching EID 2.2.2.2/32. Note that lower priority
    value has higher preference in LISP.

12. Verify the correct registration of the 2.2.2.2/32 EID:

    ::

        curl -u "admin":"admin" -H "Content-type: application/json" -X POST \
            http://localhost:8181/restconf/operations/odl-mappingservice:get-mapping \
            --data @get2.json

    where *get2.json* can be derived from *get1.json* by changing the
    content of the *Ipv4Address* field from *1.1.1.1* to *2.2.2.2*.

13. Now the LISP network is up. To verify, log into the **client** VM
    and ping the server EID:

    ::

        ping 2.2.2.2

14. Let’s test fail-over now. Suppose you had a service on **server1**
    which became unavailable, but **server1** itself is still reachable.
    LISP will not automatically fail over, even if the mapping for
    2.2.2.2/32 has two locators, since both locators are still reachable
    and uses the one with the higher priority (lowest priority value).
    To force a failover, we need to set the priority of **server2** to a
    lower value. Using the file mapping.json above, swap the priority
    values between the two locators (lines 14 and 28 in *mapping.json*)
    and repeat the request from step 11. You can also repeat step 12 to
    see if the mapping is correctly registered. If you leave the ping
    on, and monitor the traffic using wireshark, you can see that the
    ping traffic to 2.2.2.2 will be diverted from the **server1** RLOC
    to the **server2** RLOC.

    With the default OpenDaylight configuration the failover should be
    near instantaneous (we observed 3 lost pings in the worst case),
    because of the LISP `Solicit-Map-Request (SMR)
    mechanism <http://tools.ietf.org/html/rfc6830#section-6.6.2>`__ that
    can ask a LISP data plane element to update its mapping for a
    certain EID (enabled by default). It is controlled by the
    ``lisp.smr`` variable in ``etc/custom.porperties``. When enabled,
    any mapping change from the RPC interface will trigger an SMR packet
    to all data plane elements that have requested the mapping in the
    last 24 hours (this value was chosen because it’s the default TTL of
    Cisco IOS xTR mapping registrations). If disabled, ITRs keep their
    mappings until the TTL specified in the Map-Reply expires.

15. To add a service chain into the path from the client to the server,
    we can use an Explicit Locator Path, specifying the **service-node**
    as the first hop and **server1** (or **server2**) as the second hop.
    The following will achieve that:

    ::

        curl -u "admin":"admin" -H "Content-type: application/json" -X POST \
            http://localhost:8181/restconf/operations/odl-mappingservice:add-mapping \
            --data @elp.json

    where the *elp.json* file is as follows:

    .. code:: json

        {
            "input": {
                "mapping-record": {
                    "recordTtl": 1440,
                    "action": "NoAction",
                    "authoritative": true,
                    "eid": {
                        "address-type": "ietf-lisp-address-types:ipv4-prefix-afi",
                        "ipv4-prefix": "2.2.2.2/32"
                    },
                    "LocatorRecord": [
                        {
                            "locator-id": "ELP",
                            "priority": 1,
                            "weight": 1,
                            "multicastPriority": 255,
                            "multicastWeight": 0,
                            "localLocator": true,
                            "rlocProbed": false,
                            "routed": true,
                            "rloc": {
                                "address-type": "ietf-lisp-address-types:explicit-locator-path-lcaf",
                                "explicit-locator-path": {
                                    "hop": [
                                        {
                                            "hop-id": "service-node",
                                            "address": "192.168.16.33",
                                            "lrs-bits": "strict"
                                        },
                                        {
                                            "hop-id": "server1",
                                            "address": "192.168.16.31",
                                            "lrs-bits": "strict"
                                        }
                                    ]
                                }
                            }
                        }
                    ]
                }
            }
        }

    After the mapping for 2.2.2.2/32 is updated with the above, the ICMP
    traffic from **client** to **server1** will flow through the
    **service-node**. You can confirm this in the LISPmob logs, or by
    sniffing the traffic on either the **service-node** or **server1**.
    Note that service chains are unidirectional, so unless another ELP
    mapping is added for the return traffic, packets will go from
    **server1** to **client** directly.

16. Suppose the **service-node** is actually a firewall, and traffic is
    diverted there to support access control lists (ACLs). In this
    tutorial that can be emulated by using ``iptables`` firewall rules
    in the **service-node** VM. To deny traffic on the service chain
    defined above, the following rule can be added:

    ::

        iptables -A OUTPUT --dst 192.168.16.31 -j DROP

    The ping from the **client** should now have stopped.

    In this case the ACL is done on the destination RLOC. There is an
    effort underway in the LISPmob community to allow filtering on EIDs,
    which is the more logical place to apply ACLs.

17. To delete the rule and restore connectivity on the service chain,
    delete the ACL by issuing the following command:

    ::

        iptables -D OUTPUT --dst 192.168.16.31 -j DROP

    which should restore connectivity.

LISP Flow Mapping Support
-------------------------

For support the lispflowmapping project can be reached by emailing the
developer mailing list: lispflowmapping-dev@lists.opendaylight.org or on
the #opendaylight-lispflowmapping IRC channel on irc.freenode.net.

Additional information is also available on the `Lisp Flow Mapping
wiki <https://wiki.opendaylight.org/view/OpenDaylight_Lisp_Flow_Mapping:Main>`__

Messaging4Transport User Guide
==============================

Overview
--------

The OpenDaylight controller is based on an MD-SAL allows the modeling of
data, RPCs, and notifications. Because of this model basis, adding new
northbound bindings to the controller is simple, and everything modeled
becomes exposed automatically. Currently the MD-SAL has RESTCONF
northbound bindings, while more bindings such as AMQP and XMPP can
easily be implemented and integrated. Messaging4Transport attempts to
build more northbound interfaces to MD-SAL, with message-oriented
middleware protocols. Messaging4Transport Beryllium offers an AMQP
northbound to MD-SAL.

Architecture
------------

`Advanced Message Queuing Protocol (AMQP) <http://www.amqp.org>`__ is an
open standard application layer protocol for message-oriented
middleware. Messaging4Transport adds AMQP bindings to the MD-SAL, which
would automatically make all MD-SAL APIs available via that mechanism.
Messaging4Transport is built as an independent Karaf feature, that
exposes the MD-SAL data tree, RPCs, and notifications via AMQP, when
installed. While AMQP is the focus for the Beryllium Release, other
message-oriented transport protocols will be considered for future
releases.

A message broker internal or external to OpenDaylight receives the
messages that are published by the MD-SAL, and sends them to the
subscribers. Hence, the broker functions as an intermediary in messages
from the controller to the listeners, and vice versa. ActiveMQ has been
chosen as the default external broker in the Messaging4Transport
Beryllium.

Installing Karaf Features
~~~~~~~~~~~~~~~~~~~~~~~~~

Install Messaging4Transport by using the karaf console.

::

    feature:install odl-mdsal-all odl-messaging4transport-api odl-messaging4transport

ActiveMQ Integration with Karaf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ActiveMQ broker can be integrated into the Karaf environment. The
`ActiveMQ OSGi integration instructions
page <http://activemq.apache.org/osgi-integration.html>`__ is for Karaf
2.x. Please see the `Karaf updates
page <http://karaf.apache.org/manual/latest/update-notes.html>`__ for
further updates.

Since OpenDaylight Beryllium is built on Karaf 3.x, the instructions are
given below to install and activate ActiveMQ OSGi bundle into Karaf.

-  Installing ActiveMQ in Karaf feature:repo-add activemq 5.9.0

   ::

       feature:install activemq-broker

-  Installing `hawtio <http://hawt.io/getstarted/index.html>`__ in
   Karaf.

hawtio provides a user-friendly web user interface, that can be
installed optionally to work with the project.

::

    feature:repo-add hawtio 1.4.51

::

    feature:install hawtio

Administering or Managing Messaging4Transport
---------------------------------------------

The broker can be a stand-alone or a Karaf-based broker integrated into
OpenDaylight. Just install the bundles as shown below for Karaf based
integration. In such a case, broker will start with OpenDaylight. The
publisher publishes the data tree. At least a dummy listener should be
started before the publisher to receive the published messages.

You may further configure the broker by modifying the ActiveMQ
configuration file in
ODL\_INSTALLATION\_DIR/karaf/target/assembly/etc/org.apache.activemq.server-default.cfg

Make sure to set the transport connections in
karaf/target/assembly/etc/activemq.xml, which is set by default in
ActiveMQ stand-alone implementation; but not in the Karaf
implementation.

It is suggested to limit concurrent connections to just 1000. However,
probably we will need more concurrency, based on the requirements.
Setting it to 100,000 for now.

::

    <transportConnectors>
    <!-- DOS protection, limit concurrent connections to 1000 and frame size to 100MB -->
    <!-- Uncomment whatever necessary. -->
    <transportConnector name="openwire" uri="tcp://0.0.0.0:61616?maximumConnections=100000&amp;wireFormat.maxFrameSize=104857600"/>
    <transportConnector name="amqp" uri="amqp://0.0.0.0:5672?maximumConnections=100000&amp;wireFormat.maxFrameSize=104857600"/>
    <!--transportConnector name="stomp" uri="stomp://0.0.0.0:61613?maximumConnections=100000&amp;wireFormat.maxFrameSize=104857600"/ -->
    <!--transportConnector name="mqtt" uri="mqtt://0.0.0.0:1883?maximumConnections=100000&amp;wireFormat.maxFrameSize=104857600"/ -->
    <!--transportConnector name="ws" uri="ws://0.0.0.0:61614?maximumConnections=100000&amp;wireFormat.maxFrameSize=104857600"/ -->
    </transportConnectors>

You may need to install/re-install the bundle after that and restart the
container for the changes to take effort.

The MD-SAL will be the publisher that publishes the MD-SAL data tree,
RPCs, and notifications via AMQP. The listener can be any consumer that
consumes the data tree and the other data published by MD-SAL via the
AMQP binding.

Once configured, the ActiveMQ console can be accessed from the `hawtio
web console <http://localhost:8181/hawtio/>`__ with the credentials
karaf/karaf.

Messaging4Transport can hence be configured to publish MD-SAL
notifications to an external AMQP listener application through the
broker. A simple listener application is included in the
org.opendaylight.messaging4transport.sample package.

NEtwork MOdeling (NEMO)
=======================

This section describes how to use the NEMO feature in OpenDaylight and
contains contains configuration, administration, and management sections
for the feature.

Overview
--------

TBD: An overview of the NEMO feature and the use case and the audience
who will use the feature.

NEMO Engine Architecture
------------------------

TBD: Information about NEMO Engine components and how they work
together. Also include information about how the feature integrates with
OpenDaylight.

Configuring NEMO Engine
-----------------------

TBD: Describe how to configure the NEMO Engine after installation.

Administering or Managing NEMO Engine
-------------------------------------

TBD: Include related command reference or operations for using the NEMO
Engine.

Tutorials
---------

Below are tutorials for NEMO Engine.

Using NEMO Engine
~~~~~~~~~~~~~~~~~

TBD: State the purpose of tutorial

Overview
^^^^^^^^

TBD: An overview of the NEMO tutorial

Prerequisites
^^^^^^^^^^^^^

TBD: Provide any prerequisite information, assumed knowledge, or
environment required to execute the use case.

Target Environment
^^^^^^^^^^^^^^^^^^

TBD: Include any topology requirement for the use case.

Instructions
^^^^^^^^^^^^

TBD: Step by step procedure for using NEMO Engine.

NetIDE User Guide
=================

Overview
--------

OpenDaylight’s NetIDE project allows users to run SDN applications
written for different SDN controllers, e.g., Floodlight or Ryu, on top
of OpenDaylight managed infrastructure. The NetIDE Network Engine
integrates a client controller layer that executes the modules that
compose a Network Application and interfaces with a server SDN
controller layer that drives the underlying infrastructure. In addition,
it provides a uniform interface to common tools that are intended to
allow the inspection/debug of the control channel and the management of
the network resources.

The Network Engine provides a compatibility layer capable of translating
calls of the network applications running on top of the client
controllers, into calls for the server controller framework. The
communication between the client and the server layers is achieved
through the NetIDE intermediate protocol, which is an application-layer
protocol on top of TCP that transmits the network control/management
messages from the client to the server controller and vice-versa.
Between client and server controller sits the Core Layer which also
speaks the intermediate protocol.

NetIDE API
----------

Architecture and Design
~~~~~~~~~~~~~~~~~~~~~~~

The NetIDE engine follows the ONF’s proposed Client/Server SDN
Application architecture.

.. figure:: ./images/netide/netidearch.jpg
   :alt: NetIDE Network Engine Architecture

   NetIDE Network Engine Architecture

Core
~~~~

The NetIDE Core is a message-based system that allows for the exchange
of messages between OpenDaylight and subscribed Client SDN Controllers

Handling reply messages correctly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When an application module sends a request to the network (e.g. flow
statistics, features, etc.), the Network Engine must be able to
correctly drive the corresponding reply to such a module. This is not a
trivial task, as many modules may compose the network application
running on top of the Network Engine, and there is no way for the Core
to pair replies and requests. The transaction IDs (xid) in the OpenFlow
header are unusable in this case, as it may happen that different
modules use the same values.

In the proposed approach, represented in the figure below, the task of
pairing replies with requests is performed by the Shim Layer which
replaces the original xid of the OpenFlow requests coming from the core
with new unique xid values. The Shim also saves the original OpenFlow
xid value and the module id it finds in the NetIDE header. As the
network elements must use the same xid values in the replies, the Shim
layer can easily pair a reply with the correct request as it is using
unique xid values.

The below figure shows how the Network Engine should handle the
controller-to-switch OpenFlow messages. The diagram shows the case of a
request message sent by an application module to a network element where
the Backend inserts the module id of the module in the NetIDE header (X
in the Figure). For other messages generated by the client controller
platform (e.g. echo requests) or by the Backend, the module id of the
Backend is used (Y in the Figure).

.. figure:: ./images/netide/netide-flow.jpg
   :alt: NetIDE Communication Flow

   NetIDE Communication Flow

Configuration
~~~~~~~~~~~~~

Below are the configuration items which can be edited, including their
default values.

-  core-address: This is the ip address of the NetIDE Core, default is
   127.0.0.1

-  core-port: The port of on which the NetIDE core is listening on

-  address: IP address where the controller listens for switch
   connections, default is 127.0.0.1

-  port: Port where controller listens for switch connections, default:
   6644

-  transport-protocol: default is TCP

-  switch-idle-timeout: default is 15000ms

Network Intent Composition (NIC) User Guide
===========================================

Overview
--------

Network Intent Composition (NIC) is an interface that allows clients to
express a desired state in an implementation-neutral form that will be
enforced via modification of available resources under the control of
the OpenDaylight system.

This description is purposely abstract as an intent interface might
encompass network services, virtual devices, storage, etc.

The intent interface is meant to be a controller-agnostic interface so
that "intents" are portable across implementations, such as OpenDaylight
and ONOS. Thus an intent specification should not contain implementation
or technology specifics.

The intent specification will be implemented by decomposing the intent
and augmenting it with implementation specifics that are driven by local
implementation rules, policies, and/or settings.

Network Intent Composition (NIC) Architecture
---------------------------------------------

The core of the NIC architecture is the intent model, which specifies
the details of the desired state. It is the responsibility of the NIC
implementation transforms this desired state to the resources under the
control of OpenDaylight. The component that transforms the intent to the
implementation is typically referred to as a renderer.

For the Lithium release, multiple, simultaneous renderers will not be
supported. Instead either the VTN or GBP renderer feature can be
installed, but not both.

For the Litium release, the only actions supported are "ALLOW" and
"BLOCK". The "ALLOW" action indicates that traffic can flow between the
source and destination end points, while "BLOCK" prevents that flow;
although it is possible that an given implementation may augment the
available actions with additional actions.

Besides transforming a desired state to an actual state it is the
responsibility of a renderer to update the operational state tree for
the NIC data model in OpenDaylight to reflect the intent which the
renderer implemented.

Configuring Network Intent Composition (NIC)
--------------------------------------------

For the Litium release there is no default implementation of a renderer,
thus without an additional module installed the NIC will not function.

Administering or Managing Network Intent Composition (NIC)
----------------------------------------------------------

There is no additional administration of management capabilities related
to the Network Intent Composition features.

Interactions
------------

A user can interact with the Network Intent Composition (NIC) either
through the RESTful interface using standard RESTCONF operations and
syntax or via the Karaf console CLI.

REST
~~~~

Configuration
^^^^^^^^^^^^^

The Network Intent Composition (NIC) feature supports the following REST
operations against the configuration data store.

-  POST - creates a new instance of an intent in the configuration
   store, which will trigger the realization of that intent. An ID
   *must* be specified as part of this request as an attribute of the
   intent.

-  PUT - creates or updates an instance of an intent in the
   configuration store, which will trigger the realization of that
   intent.

-  GET - fetches a list of all configured intents or a specific
   configured intent.

-  DETELE - removes a configured intent from the configuration store,
   which triggers the removal of the intent from the network.

Operational
^^^^^^^^^^^

The Network Intent Composition (NIC) feature supports the following REST
operations against the operational data store.

-  GET - fetches a list of all operational intents or a specific
   operational intent.

Karaf Console CLI
~~~~~~~~~~~~~~~~~

Using the Karaf console CLI intents can be manipulated. The following
Karaf console CLI commands are available.

-  intent:add <intent-data> - creates a new intent

-  intent:update <id> <intent-data> - updates an existing intent

-  intent:list - lists all intents in the system

-  intent:show <id> - display the details of a specific intent

-  intent:delete <id> - removes an intent from the system

NIC Usage Examples
------------------

How to configure VTN Renderer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The NIC Model provides an abstract model for expressing the desired
state and operation of the network.

Requirement
^^^^^^^^^^^

-  Configure mininet and create a topology:

Replace <Controller IP> based on your environment

::

    $  mininet@mininet-vm:~$ sudo mn --controller=remote,ip=<Controller IP> --topo tree,2

::

     mininet> net
     h1 h1-eth0:s2-eth1
     h2 h2-eth0:s2-eth2
     h3 h3-eth0:s3-eth1
     h4 h4-eth0:s3-eth2
     s1 lo:  s1-eth1:s2-eth3 s1-eth2:s3-eth3
     s2 lo:  s2-eth1:h1-eth0 s2-eth2:h2-eth0 s2-eth3:s1-eth1
     s3 lo:  s3-eth1:h3-eth0 s3-eth2:h4-eth0 s3-eth3:s1-eth2
     c0

Downloading and deploy Karaf distribution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Get the Lithium Distribution.

-  Unzip the downloaded zip distribution

-  To run the Karaf

::

    ./bin/karaf

-  Once the console is up, type as below to install feature.

::

    feature:install odl-nic-renderer-vtn

Configuration
^^^^^^^^^^^^^

Please execute the following curl commands to test network intent using
mininet:

-  Create Intent

::

    curl -v --user "admin":"admin" -H "Accept: application/json" -H "Content-type: application/json" -X PUT http://localhost:8181/restconf/config/intent:intents/intent/b9a13232-525e-4d8c-be21-cd65e3436034 -d '{ "intent:intent" : { "intent:id": "b9a13232-525e-4d8c-be21-cd65e3436034", "intent:actions" : [ { "order" : 2, "allow" : {} } ], "intent:subjects" : [ { "order":1 , "end-point-group" : {"name":"10.0.0.1"} }, { "order":2 , "end-point-group" : {"name":"10.0.0.2"}} ] } }'

::

    curl -v --user "admin":"admin" -H "Accept: application/json" -H "Content-type: application/json" -X PUT http://localhost:8181/restconf/config/intent:intents/intent/b9a13232-525e-4d8c-be21-cd65e3436035 -d '{ "intent:intent" : { "intent:id": "b9a13232-525e-4d8c-be21-cd65e3436035", "intent:actions" : [ { "order" : 2, "allow" : {} } ], "intent:subjects" : [ { "order":1 , "end-point-group" : {"name":"10.0.0.2"} }, { "order":2 , "end-point-group" : {"name":"10.0.0.3"}} ] } }'

**Verification.**

::

     mininet> pingall
     Ping: testing ping reachability
     h1 -> h2 X X
     h2 -> h1 h3 X
     h3 -> X h2 X
     h4 -> X X X

-  Update an Intent

::

    curl -v --user "admin":"admin" -H "Accept: application/json" -H "Content-type: application/json" -X PUT http://localhost:8181/restconf/config/intent:intents/intent/b9a13232-525e-4d8c-be21-cd65e3436034 -d '{ "intent:intent" : { "intent:id": "b9a13232-525e-4d8c-be21-cd65e3436034", "intent:actions" : [ { "order" : 2, "block" : {} } ], "intent:subjects" : [ { "order":1 , "end-point-group" : {"name":"10.0.0.1"} }, { "order":2 , "end-point-group" : {"name":"10.0.0.2"}} ] } }'

**Verification.**

::

     mininet> pingall
     Ping: testing ping reachability
     h1 -> X X X
     h2 -> X h3 X
     h3 -> X h2 X
     h4 -> X X X

    **Note**

    Old actions and hosts are replaced by the new action and hosts.

-  Delete an Intent

::

    curl -v --user "admin":"admin" -H "Accept: application/json" -H     "Content-type: application/json" -X DELETE http://localhost:8181/restconf/config/intent:intents/intent/b9a13232-525e-4d8c-be21-cd65e3436035

**Verification.**

::

     mininet> pingall
     Ping: testing ping reachability
     h1 -> X X X
     h2 -> X X X
     h3 -> X X X
     h4 -> X X X

    **Note**

    Ping between two hosts can also be done using MAC Address

::

    curl -v --user "admin":"admin" -H "Accept: application/json" -H "Content-type: application/json" -X PUT http://localhost:8181/restconf/config/intent:intents/intent/b9a13232-525e-4d8c-be21-cd65e3436035 -d '{ "intent:intent" : { "intent:id": "b9a13232-525e-4d8c-be21-cd65e3436035", "intent:actions" : [ { "order" : 2, "allow" : {} } ], "intent:subjects" : [ { "order":1 , "end-point-group" : {"name":"6e:4f:f7:27:15:c9"} }, { "order":2 , "end-point-group" : {"name":"aa:7d:1f:4a:70:81"}} ] } }'

ODL-SDNi User Guide
===================

Introduction
------------

This user guide will help to setup the ODL-SDNi application for lithium
release and contains the examples configuration using ODL-BGPCEP.

Components
----------

SDNiAggregator(controller), SDNi REST API(controller) and
SDNiWrapper(bgpcep) are the three components in ODL-SDNi App

-  SDNiAggregator: Connects with switch, topology, hosttracker managers
   of controller to get the topology and other related data.

-  SDNi REST API: It is a part of controller northbound, which gives the
   required information by quering SDNiAggregator through RESTCONF.

-  SDNiWrapper: This component uses the SDNi REST API and gathers the
   information required to be shared among controllers.

Troubleshooting
---------------

To work with multiple controllers, change some of the configuration in
config.ini file. For example change the listening port of one controller
to 6653 and other controller to 6663 in
/root/controller/opendaylight/distribution/opendaylight/target/distribution.opendaylight-osgipackage/opendaylight/configuration/config.ini
(i.e of.listenPort=6653).

**OpenFlow related system parameters.**

TCP port on which the controller is listening (default 6633)
of.listenPort=6653

OpenFlow Plugin Project User Guide
==================================

Overview and Architecture
-------------------------

Overview and Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
^^^^^^^^

OpenFlow is a vendor-neutral standard communications interface defined
to enable interaction between the control and forwarding layers of an
SDN architecture. The OpenFlow plugin project intends to develop a
plugin to support implementations of the OpenFlow specification as it
develops and evolves. Specifically the project has developed a plugin
aiming to support OpenFlow 1.0 and 1.3.x. It can be extended to add
support for subsequent OpenFlow specifications. The plugin is based on
the Model Driven Service Abstraction Layer (MD-SAL) architecture
(https://wiki.opendaylight.org/view/OpenDaylight_Controller:MD-SAL).
This new OpenFlow 1.0/1.3 MD-SAL based plugin is distinct from the old
OpenFlow 1.0 plugin which was based on the API driven SAL (AD-SAL)
architecture.

Scope
^^^^^

-  Southbound plugin and integration of OpenFlow 1.0/1.3.x library
   project

-  Ongoing support and integration of the OpenFlow specification

-  The plugin should be implemented in an easily extensibile manner

-  Protocol verification activities will be performed on supported
   OpenFlow specifications

Architecture and Design
^^^^^^^^^^^^^^^^^^^^^^^

Functionality
'''''''''''''

OpenFlow 1.3 Plugin will support the following functionality

-  Connection Handling

-  Session Management

-  State Management.

-  Error Handling.

-  Mapping function(Infrastructure to OF structures).

-  Connection establishment will be handled by OpenFlow library using
   opensource netty.io library.

-  Message handling(Ex: Packet in).

-  Event handling and propagation to upper layers.

-  Plugin will support both MD-SAL and Hard SAL.

-  Will be backward compatible with OF 1.0.

**Activities in OF plugin module**

-  New OF plugin bundle will support both OF 1.0 and OF 1.3.

-  Integration with OpenFlow library.

-  Integration with corresponding MD-SAL infrastructure.

-  Hard SAL will be supported as adapter on top of MD-SAL plugin.

-  OF 1.3 and OF 1.0 plugin will be integrated as single bundle.

Design
''''''

**Overall Architecture**

.. figure:: ./images/openflowplugin/plugin_design.jpg
   :alt: overal architecture

   overal architecture

Coverage
~~~~~~~~

Intro
^^^^^

This page is to catalog the things that have been tested and confirmed
to work:

Coverage
^^^^^^^^

Coverage has been moved to a `GoogleDoc
Spreadshee <https://docs.google.com/spreadsheet/ccc?key=0AtpUuSEP8OyMdHNTZjBoM0VjOE9BcGhHMzk3N19uamc&usp=sharing%23gid=2#gid=0>`__

OF 1.3 Considerations
^^^^^^^^^^^^^^^^^^^^^

The baseline model is a OF 1.3 model, and the coverage tables primarily
deal with OF 1.3. However for OF 1.0, we have a column to indicate
either N/A if it doesn’t apply, or whether its been confirmed working.

OF 1.0 Considerations
^^^^^^^^^^^^^^^^^^^^^

OF 1.0 is being considered as a switch with: \* 1 Table \* 0 Groups \* 0
Meters \* 1 Instruction (Apply Actions) \* and a limited vocabulary of
matches and actions.

Tutorial / How-To
-----------------

Running the controller with the new OpenFlow Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Opendaylight Controller Plugin Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Run OpenDaylight controller with the new OpenFlow 1.0/1.3 plugin

There are 2 ways. In integration project the plugin version is
controlled by startup parameter. Or there is distribution build
available directly in openflowplugin project.

1. use **integration** project

   -  download and unzip latest build from
      https://nexus.opendaylight.org/content/repositories/opendaylight.snapshot/org/opendaylight/integration/distribution-karaf/0.2.2-SNAPSHOT/

      ::

          cd <extracted directory>/bin
          ./karaf

   -  or clone and build **integration** project:

      ::

          git clone https://git.opendaylight.org/gerrit/p/integration.git
          cd integration/distributions/extra/karaf
          mvn clean install
          cd ./target/assembly/bin

   -  and finally run

      ::

          ./karaf

2. use **openflowplugin** project

   -  download and unzip latest build from
      https://nexus.opendaylight.org/content/repositories/opendaylight.snapshot/org/opendaylight/openflowplugin/openflowplugin-karaf/0.1.0-SNAPSHOT/

      ::

          cd <extracted directory>/bin
          ./karaf

   -  or clone and build **openflowplugin** project:

      ::

          git clone https://git.opendaylight.org/gerrit/p/openflowplugin.git
          cd openflowplugin
          mvn clean install
          cd ./distribution/karaf/target/assembly/bin/

   -  or build whole distribution localy from folder distribution/karaf

      ::

          mvn clean install -DskipTests

   -  and run

      ::

          ./karaf

**How to start**

There are all helium features (from features-openflowplugin) duplicated
into features-openflowplugin-li. The duplicates got suffix *-li* and
provide Lithium codebase functionality.

These are most used:

-  odl-openflowplugin-app-lldp-speaker-li

-  odl-openflowplugin-flow-services-rest-li

-  odl-openflowplugin-drop-test-li

In case topology is required then the first one should be installed.

::

    feature:install odl-openflowplugin-app-lldp-speaker-li

The Li-southbound currently provides:

-  flow management

-  group management

-  meter management

-  statistics polling

**What to log**

In order to see really low level messages enter these in karaf console:

::

    log:set TRACE org.opendaylight.openflowplugin.openflow.md.core
    log:set TRACE org.opendaylight.openflowplugin.impl

**How enable topology**

In order for topology to work (fill dataStore/operational with links)
there must be LLDP responses delivered back to controller. This requires
table-miss-entries. Table-miss-entry is a flow in table.id=0 with low
priority, empty match and one output action = send to controller. Having
this flow installed on every node will enable for gathering and
exporting links between nodes into dataStore/operational. This is done
if you use for example l2 switch application.

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
       <barrier>false</barrier>
       <cookie>54</cookie>
       <flags>SEND_FLOW_REM</flags>
       <flow-name>FooXf54</flow-name>
       <hard-timeout>0</hard-timeout>
       <id>4242</id>
       <idle-timeout>0</idle-timeout>
       <installHw>false</installHw>
       <instructions>
           <instruction>
               <apply-actions>
                   <action>
                       <output-action>
                           <max-length>65535</max-length>
                           <output-node-connector>CONTROLLER</output-node-connector>
                       </output-action>
                       <order>0</order>
                   </action>
               </apply-actions>
               <order>0</order>
           </instruction>
       </instructions>
       <match/>
       <priority>0</priority>
       <strict>false</strict>
       <table_id>0</table_id>
    </flow>

**Enable RESTCONF and Controller GUI**

If you want to use RESTCONF with openflowplugin project, you have to
install *odl-restconf* feature to enable that. To install *odl-restconf*
feature run the following command

::

    karaf#>feature:install odl-restconf

If you want to access the Controller GUI, you have to install
*odl-dlux-core* feature to enable that. Run following command to install
it

::

    karaf#>feature:install odl-dlux-core

Once you enable the feature, access the Controller GUI using following
URL

::

    http://<controller-ip>:8181/dlux/index.html

**Run OpenDaylight controller with the old OpenFlow 1.0-only (old)
plugin**

There are 2 ways. In integration project the plugin version is
controlled by startup parameter. Or there is distribution build
available directly in controller project.

1. use **integration/distributions/base** project

   -  use the instructions from
      OpenDaylight\_OpenFlow\_Plugin::Running\_controller\_with\_the\_new\_OF\_plugin#To\_run\_the\_OpenDaylight\_controller\_with\_the\_new\_OpenFlow\_1.0/1.3\_(new)\_plugin[
      1.0/1.3 plugin], but skip the plugin version parameter:

      ::

          ./run.sh

2. use **controller/distribution/opendaylight** project

   -  download and unzip latest build from
      https://nexus.opendaylight.org/content/repositories/opendaylight.snapshot/org/opendaylight/controller/distribution.opendaylight/

      ::

          cd opendaylight

   -  or clone and build **controller** project:

      ::

          git clone https://git.opendaylight.org/gerrit/p/controller.git
          cd controller/opendaylight/distribution/opendaylight
          mvn clean install
          cd target/distribution.opendaylight-osgipackage/opendaylight

   -  and finally run (there is no version specific option, because the

      1.0/1.3 (new) plugin is not available here at all)

**Give it a minute to come up :)**

OpenFlow 1.3 Enabled Software Switches / Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Getting Mininet with OF 1.3
^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Download Mininet VM Upgraded to OF
1.3 <https://www.dropbox.com/s/dbf9a372elqs1s1/mininet-of-1.3.zip>`__
(or the `newer mininet-2.1.0 with
OVS-2.0 <https://www.dropbox.com/s/t66vqfqx57a7nhk/mininet-2.1.0-of1.3.zip>`__
that works with VMware Player. For using this on VirtualBox, import this
to VMware Player and then export the .vmdk ) or you could build one
yourself Openflow Protocol Library:OpenVirtualSwitch[Instructions for
setting up Mininet with OF 1.3].

Installing under VirtualBox
'''''''''''''''''''''''''''

.. figure:: ./images/openflowplugin/host-only-vbox.png
   :alt: configuring a host-only adapter

   configuring a host-only adapter

For whatever reason, at least on the Mac, NATed interfaces in VirtualBox
don’t actually seem to allow for connections from the host to the VM.
Instead, you need to configure a host-only network and set it up. Do
this by:

-  Go to the VM’s settings in VirtualBox then to network and add a
   second adapter attached to "Host-only Adapter" (see the screenshot to
   the right)

-  Edit the /etc/network/interfaces file to configure the adapter
   properly by adding these two lines

::

    auto eth1
    iface eth1 inet dhcp

-  Reboot the VM

At this point you should have two interfaces one which gives you NATed
access to the internet and another that gives you access between your
mac and the VMs. At least for me, the NATed interface gets a 10.0.2.x
address and the the host-only interface gets a 192.168.56.x address.

Your simplest choice: Use Vagrant
'''''''''''''''''''''''''''''''''

`Download Virtual Box <https://www.virtualbox.org/>`__ and install it
`Download Vagrant <http://www.vagrantup.com/>`__ and install it

::

    cd openflowplugin/vagrant/mininet-2.1.0-of-1.3/
    vagrant up
    vagrant ssh

This will leave you sshed into a fully provisioned Ubuntu Trusty box
with mininet-2.1.0 and OVS 2.0 patches to work with OF 1.3.

Setup CPqD Openflow 1.3 Soft Switch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Latest version of Openvswitch (v2.0.0) doesn’t support all the openflow
1.3 features, e.g group multipart statistics request. Alternate options
is CPqD Openflow 1.3 soft switch, It supports most of the openflow 1.3
features.

-  You can setup the switch as per the instructions given on the
   following URL

```https://github.com/CPqD/ofsoftswitch13`` <https://github.com/CPqD/ofsoftswitch13>`__

-  Fire following command to start the switch

Start the datapath :

::

    $ sudo udatapath/ofdatapath --datapath-id=<dpid> --interfaces=<if-list> ptcp:<port>
     e.g $ sudo udatapath/ofdatapath --datapath-id=000000000001 --interfaces=ethX ptcp:6680

ethX should not be associated with ip address and ipv6 should be
disabled on it. If you are installing the switch on your local machine,
you can use following command (for Ubuntu) to create virtual interface.

::

    ip link add link ethX address 00:19:d1:29:d2:58 macvlan0 type macvlan

ethX - Any existing interface.

Or if you are using mininet VM for installing this switch, you can
simply add one more adaptor to your VM.

Start Openflow protocol agent:

::

    $secchan/ofprotocol tcp:<switch-host>:<switch-port> tcp:<ctrl-host>:<ctrl-port>
     e.g $secchan/ofprotocol tcp:127.0.0.1:6680 tcp:127.0.0.1:6653

Commands to add entries to various tables of the switch
'''''''''''''''''''''''''''''''''''''''''''''''''''''''

-  Add meter

::

    $utilities/dpctl tcp:<switch-host>:<switch-port> meter-mod cmd=add,meter=1 drop:rate=50

-  Add Groups

::

    $utilities/dpctl tcp:127.0.0.1:6680 group-mod cmd=add,type=all,group=1

::

    $utilities/dpctl tcp:127.0.0.1:6680 group-mod cmd=add,type=sel,group=2 weight=10 output:1

-  Create queue

::

    $utilities/dpctl tcp:<ip>:<switch port> queue-mod <port-number> <queue-number> <minimum-bandwidth>
      e.g - $utilities/dpctl tcp:127.0.0.1:6680 queue-mod 1 1 23

"dpctl" --help is not very intuitive, so please keep adding any new
command you figured out while your experiment with the switch.

Using the built-in Wireshark
''''''''''''''''''''''''''''

Mininet comes with pre-installed Wireshark, but for some reason it does
not include the Openflow protocol dissector. You may want to get and
install it in the */.wireshark/plugins/* directory.

First login to your mininet VM

::

     ssh mininet@<your mininet vm ip> -X

The -X option in ssh will enable x-session over ssh so that the
wireshark window can be shown on your host machine’s display. when
prompted, enter the password (mininet).

From the mininet vm shell, set the wireshark capture privileges
(http://wiki.wireshark.org/CaptureSetup/CapturePrivileges):

::

    sudo chgrp mininet /usr/bin/dumpcap
    sudo chmod 754 /usr/bin/dumpcap
    sudo setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap

Finally, start wireshark:

::

     wireshark

The wireshark window should show up.

To see only Openflow packets, you may want to apply the following filter
in the Filter window:

::

     tcp.port == 6633 and tcp.flags.push == 1

Start the capture on *any* port.

Running Mininet with OF 1.3
^^^^^^^^^^^^^^^^^^^^^^^^^^^

From within the Mininet VM, run:

::

     sudo mn --topo single,3  --controller 'remote,ip=<your controller ip>,port=6653' --switch ovsk,protocols=OpenFlow13

End to End Inventory
~~~~~~~~~~~~~~~~~~~~

Introduction
^^^^^^^^^^^^

The purpose of this page is to walk you through how to see the Inventory
Manager working end to end with the openflowplugin using OpenFlow 1.3.

Basically, you will learn how to:

1. Run the Base/Virtualization/Service provider Edition with the new
   openflowplugin:
   OpenDaylight\_OpenFlow\_Plugin::Running\_controller\_with\_the\_new\_OF\_plugin[Running
   the controller with the new OpenFlow Plugin]

2. Start mininet to use OF 1.3:
   OpenDaylight\_OpenFlow\_Plugin::Test\_Environment[OpenFlow 1.3
   Enabled Software Switches / Environment]

3. Use RESTCONF to see the nodes appear in inventory.

Restconf for Inventory
^^^^^^^^^^^^^^^^^^^^^^

The REST url for listing all the nodes is:

::

    http://localhost:8181/restconf/operational/opendaylight-inventory:nodes/

You will need to set the Accept header:

::

    Accept: application/xml

You will also need to use HTTP Basic Auth with username: admin password:
admin.

Alternately, if you have a node’s id you can address it as

::

    http://localhost:8181/restconf/operational/opendaylight-inventory:nodes/node/<id>

for example

::

    http://localhost:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1

How to hit RestConf with Postman
''''''''''''''''''''''''''''''''

`Install Postman for
Chrome <https://chrome.google.com/webstore/detail/postman-rest-client/fdmmgilgnpjigdojojpjoooidkmcomcm?hl=en>`__

In the chrome browser bar enter

::

    chrome://apps/

And click on Postman.

Enter the URL. Click on the Headers button on the far right. Enter the
Accept: header. Click on the Basic Auth Tab at the top and setup the
username and password. Send.

Known Bug
^^^^^^^^^

If you have not had any switches come up, and though no children for
http://localhost:8080/restconf/datastore/opendaylight-inventory:nodes/
and exception will be thrown. I’m pretty sure I know how to fix this
bug, just need to get to it :)

End to End Flows
~~~~~~~~~~~~~~~~

Instructions
^^^^^^^^^^^^

Learn End to End for Inventory
''''''''''''''''''''''''''''''

`End to End
Inventory <#odl-ofp-end-to-end-inventory_introduction-introduction>`__

Check inventory
'''''''''''''''

-  Run mininet with support for OF 1.3 as described in `End to End
   Inventory <#odl-ofp-end-to-end-inventory_introduction-introduction>`__

-  Make sure you see the openflow:1 node come up as described in `End to
   End
   Inventory <#odl-ofp-end-to-end-inventory_introduction-introduction>`__

Flow Strategy
'''''''''''''

Current way to flush a flow to switch looks like this:

1. Create MD-SAL modeled flow and commit it into dataStore using two
   phase commit `MD-SAL
   FAQ <https://wiki.opendaylight.org/view/OpenDaylight_Controller:MD-SAL:FAQ>`__

2. FRM gets notified and invokes corresponding rpc (addFlow) on
   particular service provider (if suitable provider for given node
   registered)

3. The provider (plugin in this case) transforms MD-SAL modeled flow
   into OF-API modeled flow

4. OF-API modeled flow is then flushed into OFLibrary

5. OFLibrary encodes flow into particular version of wire protocol and
   sends it to particular switch

6. Check on mininet side if flow is set

Push your flow
''''''''''''''

-  With PostMan:

   -  Set headers:

      -  Content-Type: application/xml

      -  Accept: application/xml

      -  Authentication

   -  Use URL: "http://<controller
      IP>:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow/1"

   -  PUT

   -  Use Body:

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <priority>2</priority>
        <flow-name>Foo</flow-name>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
            </ethernet-match>
            <ipv4-destination>10.0.10.2/24</ipv4-destination>
        </match>
        <id>1</id>
        <table_id>0</table_id>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                       <order>0</order>
                       <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
    </flow>

**\*Note**: If you want to try a different flow id or a different table,
make sure the URL and the body stay in sync. For example, if you wanted
to try: table 2 flow 20 you’d change the URL to:

"http://<controller
IP>:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/2/flow/20"

but you would also need to update the 20 and 2 in the body of the XML.

Other caveat, we have a known bug with updates, so please only write to
a given flow id and table id on a given node once at this time until we
resolve it. Or you can use the DELETE method with the same URL in
PostMan to delete the flow information on switch and controller cache.

Check for your flow on the switch
'''''''''''''''''''''''''''''''''

-  See your flow on your mininet:

::

    mininet@mininet-vm:~$ sudo ovs-ofctl -O OpenFlow13 dump-flows s1
    OFPST_FLOW reply (OF1.3) (xid=0x2):
    cookie=0x0, duration=7.325s, table=0, n_packets=0, n_bytes=0, idle_timeout=300, hard_timeout=600, send_flow_rem priority=2,ip,nw_dst=10.0.10.0/24 actions=dec_ttl

If you want to see the above information from the mininet prompt - use
"sh" instead of "sudo" i.e. use "sh ovs-ofctl -O OpenFlow13 dump-flows
s1".

Check for your flow in the controller config via RESTCONF
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

-  See your configured flow in POSTMAN with

   -  URL `http://<controller <http://<controller>`__
      IP>:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/table/0/

   -  GET

   -  You no longer need to set Accept header

Return Response:

.. code:: json

    {
      "flow-node-inventory:table": [
        {
          "flow-node-inventory:id": 0,
          "flow-node-inventory:flow": [
            {
              "flow-node-inventory:priority": 1,
              "flow-node-inventory:id": "10b1a23c-5299-4f7b-83d6-563bab472754",
              "flow-node-inventory:table_id": 0,
              "flow-node-inventory:hard-timeout": 0,
              "flow-node-inventory:idle-timeout": 0,
              "flow-node-inventory:instructions": {
                "flow-node-inventory:instruction": [
                  {
                    "flow-node-inventory:apply-actions": {
                      "flow-node-inventory:action": [
                        {
                          "flow-node-inventory:output-action": {
                            "flow-node-inventory:output-node-connector": "openflow:1:1"
                          },
                          "flow-node-inventory:order": 0
                        }
                      ]
                    },
                    "flow-node-inventory:order": 0
                  }
                ]
              },
              "flow-node-inventory:match": {
                "flow-node-inventory:ethernet-match": {
                  "flow-node-inventory:ethernet-type": {
                    "flow-node-inventory:type": 2048
                  }
                },
                "flow-node-inventory:ipv4-destination": "10.0.0.2"
              },
              "flow-node-inventory:cookie": 0
            },
            {
              "flow-node-inventory:priority": 1,
              "flow-node-inventory:id": "020bf359-1299-4da6-b4f7-368bd83b5841",
              "flow-node-inventory:table_id": 0,
              "flow-node-inventory:hard-timeout": 0,
              "flow-node-inventory:idle-timeout": 0,
              "flow-node-inventory:instructions": {
                "flow-node-inventory:instruction": [
                  {
                    "flow-node-inventory:apply-actions": {
                      "flow-node-inventory:action": [
                        {
                          "flow-node-inventory:output-action": {
                            "flow-node-inventory:output-node-connector": "openflow:1:1"
                          },
                          "flow-node-inventory:order": 0
                        }
                      ]
                    },
                    "flow-node-inventory:order": 0
                  }
                ]
              },
              "flow-node-inventory:match": {
                "flow-node-inventory:ethernet-match": {
                  "flow-node-inventory:ethernet-type": {
                    "flow-node-inventory:type": 2048
                  }
                },
                "flow-node-inventory:ipv4-destination": "10.0.0.1"
              },
              "flow-node-inventory:cookie": 0
            },
            {
              "flow-node-inventory:priority": 1,
              "flow-node-inventory:id": "42172bfc-9142-4a92-9e90-ee62529b1e85",
              "flow-node-inventory:table_id": 0,
              "flow-node-inventory:hard-timeout": 0,
              "flow-node-inventory:idle-timeout": 0,
              "flow-node-inventory:instructions": {
                "flow-node-inventory:instruction": [
                  {
                    "flow-node-inventory:apply-actions": {
                      "flow-node-inventory:action": [
                        {
                          "flow-node-inventory:output-action": {
                            "flow-node-inventory:output-node-connector": "openflow:1:1"
                          },
                          "flow-node-inventory:order": 0
                        }
                      ]
                    },
                    "flow-node-inventory:order": 0
                  }
                ]
              },
              "flow-node-inventory:match": {
                "flow-node-inventory:ethernet-match": {
                  "flow-node-inventory:ethernet-type": {
                    "flow-node-inventory:type": 2048
                  }
                },
                "flow-node-inventory:ipv4-destination": "10.0.0.3"
              },
              "flow-node-inventory:cookie": 0
            },
            {
              "flow-node-inventory:priority": 1,
              "flow-node-inventory:id": "99bf566e-89f3-4c6f-ae9e-e26012ceb1e4",
              "flow-node-inventory:table_id": 0,
              "flow-node-inventory:hard-timeout": 0,
              "flow-node-inventory:idle-timeout": 0,
              "flow-node-inventory:instructions": {
                "flow-node-inventory:instruction": [
                  {
                    "flow-node-inventory:apply-actions": {
                      "flow-node-inventory:action": [
                        {
                          "flow-node-inventory:output-action": {
                            "flow-node-inventory:output-node-connector": "openflow:1:1"
                          },
                          "flow-node-inventory:order": 0
                        }
                      ]
                    },
                    "flow-node-inventory:order": 0
                  }
                ]
              },
              "flow-node-inventory:match": {
                "flow-node-inventory:ethernet-match": {
                  "flow-node-inventory:ethernet-type": {
                    "flow-node-inventory:type": 2048
                  }
                },
                "flow-node-inventory:ipv4-destination": "10.0.0.4"
              },
              "flow-node-inventory:cookie": 0
            },
            {
              "flow-node-inventory:priority": 1,
              "flow-node-inventory:id": "019dcc2e-5b4f-44f0-90cc-de490294b862",
              "flow-node-inventory:table_id": 0,
              "flow-node-inventory:hard-timeout": 0,
              "flow-node-inventory:idle-timeout": 0,
              "flow-node-inventory:instructions": {
                "flow-node-inventory:instruction": [
                  {
                    "flow-node-inventory:apply-actions": {
                      "flow-node-inventory:action": [
                        {
                          "flow-node-inventory:output-action": {
                            "flow-node-inventory:output-node-connector": "openflow:1:2"
                          },
                          "flow-node-inventory:order": 0
                        }
                      ]
                    },
                    "flow-node-inventory:order": 0
                  }
                ]
              },
              "flow-node-inventory:match": {
                "flow-node-inventory:ethernet-match": {
                  "flow-node-inventory:ethernet-type": {
                    "flow-node-inventory:type": 2048
                  }
                },
                "flow-node-inventory:ipv4-destination": "10.0.0.5"
              },
              "flow-node-inventory:cookie": 0
            },
            {
              "flow-node-inventory:priority": 1,
              "flow-node-inventory:id": "968cf81e-3f16-42f1-8b16-d01ff719c63c",
              "flow-node-inventory:table_id": 0,
              "flow-node-inventory:hard-timeout": 0,
              "flow-node-inventory:idle-timeout": 0,
              "flow-node-inventory:instructions": {
                "flow-node-inventory:instruction": [
                  {
                    "flow-node-inventory:apply-actions": {
                      "flow-node-inventory:action": [
                        {
                          "flow-node-inventory:output-action": {
                            "flow-node-inventory:output-node-connector": "openflow:1:2"
                          },
                          "flow-node-inventory:order": 0
                        }
                      ]
                    },
                    "flow-node-inventory:order": 0
                  }
                ]
              },
              "flow-node-inventory:match": {
                "flow-node-inventory:ethernet-match": {
                  "flow-node-inventory:ethernet-type": {
                    "flow-node-inventory:type": 2048
                  }
                },
                "flow-node-inventory:ipv4-destination": "10.0.0.8"
              },
              "flow-node-inventory:cookie": 0
            },
            {
              "flow-node-inventory:priority": 1,
              "flow-node-inventory:id": "1c14ea3c-9dcc-4434-b566-7e99033ea252",
              "flow-node-inventory:table_id": 0,
              "flow-node-inventory:hard-timeout": 0,
              "flow-node-inventory:idle-timeout": 0,
              "flow-node-inventory:instructions": {
                "flow-node-inventory:instruction": [
                  {
                    "flow-node-inventory:apply-actions": {
                      "flow-node-inventory:action": [
                        {
                          "flow-node-inventory:output-action": {
                            "flow-node-inventory:output-node-connector": "openflow:1:2"
                          },
                          "flow-node-inventory:order": 0
                        }
                      ]
                    },
                    "flow-node-inventory:order": 0
                  }
                ]
              },
              "flow-node-inventory:match": {
                "flow-node-inventory:ethernet-match": {
                  "flow-node-inventory:ethernet-type": {
                    "flow-node-inventory:type": 2048
                  }
                },
                "flow-node-inventory:ipv4-destination": "10.0.0.6"
              },
              "flow-node-inventory:cookie": 0
            },
            {
              "flow-node-inventory:priority": 1,
              "flow-node-inventory:id": "ed9deeb2-be8f-4b84-bcd8-9d12049383d6",
              "flow-node-inventory:table_id": 0,
              "flow-node-inventory:hard-timeout": 0,
              "flow-node-inventory:idle-timeout": 0,
              "flow-node-inventory:instructions": {
                "flow-node-inventory:instruction": [
                  {
                    "flow-node-inventory:apply-actions": {
                      "flow-node-inventory:action": [
                        {
                          "flow-node-inventory:output-action": {
                            "flow-node-inventory:output-node-connector": "openflow:1:2"
                          },
                          "flow-node-inventory:order": 0
                        }
                      ]
                    },
                    "flow-node-inventory:order": 0
                  }
                ]
              },
              "flow-node-inventory:match": {
                "flow-node-inventory:ethernet-match": {
                  "flow-node-inventory:ethernet-type": {
                    "flow-node-inventory:type": 2048
                  }
                },
                "flow-node-inventory:ipv4-destination": "10.0.0.7"
              },
              "flow-node-inventory:cookie": 0
            }
          ]
        }
      ]
    }

Look for your flow stats in the controller operational data via
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

RESTCONF

-  See your operational flow stats in POSTMAN with

   -  URL "http://<controller
      IP>:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/table/0/"

   -  GET

Return Response:

.. code:: json

    {
      "flow-node-inventory:table": [
        {
          "flow-node-inventory:id": 0,
          "flow-node-inventory:flow": [
            {
              "flow-node-inventory:id": "10b1a23c-5299-4f7b-83d6-563bab472754",
              "opendaylight-flow-statistics:flow-statistics": {
                "opendaylight-flow-statistics:cookie": 0,
                "opendaylight-flow-statistics:duration": {
                  "opendaylight-flow-statistics:nanosecond": 886000000,
                  "opendaylight-flow-statistics:second": 2707
                },
                "opendaylight-flow-statistics:hard-timeout": 0,
                "opendaylight-flow-statistics:byte-count": 784,
                "opendaylight-flow-statistics:match": {
                  "opendaylight-flow-statistics:ethernet-match": {
                    "opendaylight-flow-statistics:ethernet-type": {
                      "opendaylight-flow-statistics:type": 2048
                    }
                  },
                  "opendaylight-flow-statistics:ipv4-destination": "10.0.0.2/32"
                },
                "opendaylight-flow-statistics:priority": 1,
                "opendaylight-flow-statistics:packet-count": 8,
                "opendaylight-flow-statistics:table_id": 0,
                "opendaylight-flow-statistics:idle-timeout": 0,
                "opendaylight-flow-statistics:instructions": {
                  "opendaylight-flow-statistics:instruction": [
                    {
                      "opendaylight-flow-statistics:order": 0,
                      "opendaylight-flow-statistics:apply-actions": {
                        "opendaylight-flow-statistics:action": [
                          {
                            "opendaylight-flow-statistics:order": 0,
                            "opendaylight-flow-statistics:output-action": {
                              "opendaylight-flow-statistics:output-node-connector": "1",
                              "opendaylight-flow-statistics:max-length": 0
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            },
            {
              "flow-node-inventory:id": "020bf359-1299-4da6-b4f7-368bd83b5841",
              "opendaylight-flow-statistics:flow-statistics": {
                "opendaylight-flow-statistics:cookie": 0,
                "opendaylight-flow-statistics:duration": {
                  "opendaylight-flow-statistics:nanosecond": 826000000,
                  "opendaylight-flow-statistics:second": 2711
                },
                "opendaylight-flow-statistics:hard-timeout": 0,
                "opendaylight-flow-statistics:byte-count": 1568,
                "opendaylight-flow-statistics:match": {
                  "opendaylight-flow-statistics:ethernet-match": {
                    "opendaylight-flow-statistics:ethernet-type": {
                      "opendaylight-flow-statistics:type": 2048
                    }
                  },
                  "opendaylight-flow-statistics:ipv4-destination": "10.0.0.1/32"
                },
                "opendaylight-flow-statistics:priority": 1,
                "opendaylight-flow-statistics:packet-count": 16,
                "opendaylight-flow-statistics:table_id": 0,
                "opendaylight-flow-statistics:idle-timeout": 0,
                "opendaylight-flow-statistics:instructions": {
                  "opendaylight-flow-statistics:instruction": [
                    {
                      "opendaylight-flow-statistics:order": 0,
                      "opendaylight-flow-statistics:apply-actions": {
                        "opendaylight-flow-statistics:action": [
                          {
                            "opendaylight-flow-statistics:order": 0,
                            "opendaylight-flow-statistics:output-action": {
                              "opendaylight-flow-statistics:output-node-connector": "1",
                              "opendaylight-flow-statistics:max-length": 0
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            },
            {
              "flow-node-inventory:id": "42172bfc-9142-4a92-9e90-ee62529b1e85",
              "opendaylight-flow-statistics:flow-statistics": {
                "opendaylight-flow-statistics:cookie": 0,
                "opendaylight-flow-statistics:duration": {
                  "opendaylight-flow-statistics:nanosecond": 548000000,
                  "opendaylight-flow-statistics:second": 2708
                },
                "opendaylight-flow-statistics:hard-timeout": 0,
                "opendaylight-flow-statistics:byte-count": 784,
                "opendaylight-flow-statistics:match": {
                  "opendaylight-flow-statistics:ethernet-match": {
                    "opendaylight-flow-statistics:ethernet-type": {
                      "opendaylight-flow-statistics:type": 2048
                    }
                  },
                  "opendaylight-flow-statistics:ipv4-destination": "10.0.0.3/32"
                },
                "opendaylight-flow-statistics:priority": 1,
                "opendaylight-flow-statistics:packet-count": 8,
                "opendaylight-flow-statistics:table_id": 0,
                "opendaylight-flow-statistics:idle-timeout": 0,
                "opendaylight-flow-statistics:instructions": {
                  "opendaylight-flow-statistics:instruction": [
                    {
                      "opendaylight-flow-statistics:order": 0,
                      "opendaylight-flow-statistics:apply-actions": {
                        "opendaylight-flow-statistics:action": [
                          {
                            "opendaylight-flow-statistics:order": 0,
                            "opendaylight-flow-statistics:output-action": {
                              "opendaylight-flow-statistics:output-node-connector": "1",
                              "opendaylight-flow-statistics:max-length": 0
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            },
            {
              "flow-node-inventory:id": "99bf566e-89f3-4c6f-ae9e-e26012ceb1e4",
              "opendaylight-flow-statistics:flow-statistics": {
                "opendaylight-flow-statistics:cookie": 0,
                "opendaylight-flow-statistics:duration": {
                  "opendaylight-flow-statistics:nanosecond": 296000000,
                  "opendaylight-flow-statistics:second": 2710
                },
                "opendaylight-flow-statistics:hard-timeout": 0,
                "opendaylight-flow-statistics:byte-count": 1274,
                "opendaylight-flow-statistics:match": {
                  "opendaylight-flow-statistics:ethernet-match": {
                    "opendaylight-flow-statistics:ethernet-type": {
                      "opendaylight-flow-statistics:type": 2048
                    }
                  },
                  "opendaylight-flow-statistics:ipv4-destination": "10.0.0.4/32"
                },
                "opendaylight-flow-statistics:priority": 1,
                "opendaylight-flow-statistics:packet-count": 13,
                "opendaylight-flow-statistics:table_id": 0,
                "opendaylight-flow-statistics:idle-timeout": 0,
                "opendaylight-flow-statistics:instructions": {
                  "opendaylight-flow-statistics:instruction": [
                    {
                      "opendaylight-flow-statistics:order": 0,
                      "opendaylight-flow-statistics:apply-actions": {
                        "opendaylight-flow-statistics:action": [
                          {
                            "opendaylight-flow-statistics:order": 0,
                            "opendaylight-flow-statistics:output-action": {
                              "opendaylight-flow-statistics:output-node-connector": "1",
                              "opendaylight-flow-statistics:max-length": 0
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            },
            {
              "flow-node-inventory:id": "019dcc2e-5b4f-44f0-90cc-de490294b862",
              "opendaylight-flow-statistics:flow-statistics": {
                "opendaylight-flow-statistics:cookie": 0,
                "opendaylight-flow-statistics:duration": {
                  "opendaylight-flow-statistics:nanosecond": 392000000,
                  "opendaylight-flow-statistics:second": 2711
                },
                "opendaylight-flow-statistics:hard-timeout": 0,
                "opendaylight-flow-statistics:byte-count": 1470,
                "opendaylight-flow-statistics:match": {
                  "opendaylight-flow-statistics:ethernet-match": {
                    "opendaylight-flow-statistics:ethernet-type": {
                      "opendaylight-flow-statistics:type": 2048
                    }
                  },
                  "opendaylight-flow-statistics:ipv4-destination": "10.0.0.5/32"
                },
                "opendaylight-flow-statistics:priority": 1,
                "opendaylight-flow-statistics:packet-count": 15,
                "opendaylight-flow-statistics:table_id": 0,
                "opendaylight-flow-statistics:idle-timeout": 0,
                "opendaylight-flow-statistics:instructions": {
                  "opendaylight-flow-statistics:instruction": [
                    {
                      "opendaylight-flow-statistics:order": 0,
                      "opendaylight-flow-statistics:apply-actions": {
                        "opendaylight-flow-statistics:action": [
                          {
                            "opendaylight-flow-statistics:order": 0,
                            "opendaylight-flow-statistics:output-action": {
                              "opendaylight-flow-statistics:output-node-connector": "2",
                              "opendaylight-flow-statistics:max-length": 0
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            },
            {
              "flow-node-inventory:id": "968cf81e-3f16-42f1-8b16-d01ff719c63c",
              "opendaylight-flow-statistics:flow-statistics": {
                "opendaylight-flow-statistics:cookie": 0,
                "opendaylight-flow-statistics:duration": {
                  "opendaylight-flow-statistics:nanosecond": 344000000,
                  "opendaylight-flow-statistics:second": 2707
                },
                "opendaylight-flow-statistics:hard-timeout": 0,
                "opendaylight-flow-statistics:byte-count": 784,
                "opendaylight-flow-statistics:match": {
                  "opendaylight-flow-statistics:ethernet-match": {
                    "opendaylight-flow-statistics:ethernet-type": {
                      "opendaylight-flow-statistics:type": 2048
                    }
                  },
                  "opendaylight-flow-statistics:ipv4-destination": "10.0.0.8/32"
                },
                "opendaylight-flow-statistics:priority": 1,
                "opendaylight-flow-statistics:packet-count": 8,
                "opendaylight-flow-statistics:table_id": 0,
                "opendaylight-flow-statistics:idle-timeout": 0,
                "opendaylight-flow-statistics:instructions": {
                  "opendaylight-flow-statistics:instruction": [
                    {
                      "opendaylight-flow-statistics:order": 0,
                      "opendaylight-flow-statistics:apply-actions": {
                        "opendaylight-flow-statistics:action": [
                          {
                            "opendaylight-flow-statistics:order": 0,
                            "opendaylight-flow-statistics:output-action": {
                              "opendaylight-flow-statistics:output-node-connector": "2",
                              "opendaylight-flow-statistics:max-length": 0
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            },
            {
              "flow-node-inventory:id": "ed9deeb2-be8f-4b84-bcd8-9d12049383d6",
              "opendaylight-flow-statistics:flow-statistics": {
                "opendaylight-flow-statistics:cookie": 0,
                "opendaylight-flow-statistics:duration": {
                  "opendaylight-flow-statistics:nanosecond": 577000000,
                  "opendaylight-flow-statistics:second": 2706
                },
                "opendaylight-flow-statistics:hard-timeout": 0,
                "opendaylight-flow-statistics:byte-count": 784,
                "opendaylight-flow-statistics:match": {
                  "opendaylight-flow-statistics:ethernet-match": {
                    "opendaylight-flow-statistics:ethernet-type": {
                      "opendaylight-flow-statistics:type": 2048
                    }
                  },
                  "opendaylight-flow-statistics:ipv4-destination": "10.0.0.7/32"
                },
                "opendaylight-flow-statistics:priority": 1,
                "opendaylight-flow-statistics:packet-count": 8,
                "opendaylight-flow-statistics:table_id": 0,
                "opendaylight-flow-statistics:idle-timeout": 0,
                "opendaylight-flow-statistics:instructions": {
                  "opendaylight-flow-statistics:instruction": [
                    {
                      "opendaylight-flow-statistics:order": 0,
                      "opendaylight-flow-statistics:apply-actions": {
                        "opendaylight-flow-statistics:action": [
                          {
                            "opendaylight-flow-statistics:order": 0,
                            "opendaylight-flow-statistics:output-action": {
                              "opendaylight-flow-statistics:output-node-connector": "2",
                              "opendaylight-flow-statistics:max-length": 0
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            },
            {
              "flow-node-inventory:id": "1c14ea3c-9dcc-4434-b566-7e99033ea252",
              "opendaylight-flow-statistics:flow-statistics": {
                "opendaylight-flow-statistics:cookie": 0,
                "opendaylight-flow-statistics:duration": {
                  "opendaylight-flow-statistics:nanosecond": 659000000,
                  "opendaylight-flow-statistics:second": 2705
                },
                "opendaylight-flow-statistics:hard-timeout": 0,
                "opendaylight-flow-statistics:byte-count": 784,
                "opendaylight-flow-statistics:match": {
                  "opendaylight-flow-statistics:ethernet-match": {
                    "opendaylight-flow-statistics:ethernet-type": {
                      "opendaylight-flow-statistics:type": 2048
                    }
                  },
                  "opendaylight-flow-statistics:ipv4-destination": "10.0.0.6/32"
                },
                "opendaylight-flow-statistics:priority": 1,
                "opendaylight-flow-statistics:packet-count": 8,
                "opendaylight-flow-statistics:table_id": 0,
                "opendaylight-flow-statistics:idle-timeout": 0,
                "opendaylight-flow-statistics:instructions": {
                  "opendaylight-flow-statistics:instruction": [
                    {
                      "opendaylight-flow-statistics:order": 0,
                      "opendaylight-flow-statistics:apply-actions": {
                        "opendaylight-flow-statistics:action": [
                          {
                            "opendaylight-flow-statistics:order": 0,
                            "opendaylight-flow-statistics:output-action": {
                              "opendaylight-flow-statistics:output-node-connector": "2",
                              "opendaylight-flow-statistics:max-length": 0
                            }
                          }
                        ]
                      }
                    }
                  ]
                }
              }
            }
          ],
          "opendaylight-flow-table-statistics:flow-table-statistics": {
            "opendaylight-flow-table-statistics:active-flows": 8,
            "opendaylight-flow-table-statistics:packets-matched": 97683,
            "opendaylight-flow-table-statistics:packets-looked-up": 101772
          }
        }
      ]
    }

Discovering and testing new Flow Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently, the openflowplugin has a test-provider that allows you to
push various flows through the system from the OSGI command line. Once
those flows have been pushed through, you can see them as examples and
then use them to see in the config what a particular flow example looks
like.

Using addMDFlow
'''''''''''''''

From the

::

    cd openflowplugin/distribution/base/target/distributions-openflowplugin-base-0.0.1-SNAPSHOT-osgipackage/opendaylight
    ./run.sh

Point your mininet at the controller as described above.

once you can see your node (probably openflow:1 if you’ve been following
along) in the inventory, at the OSGI command line try running:

::

    addMDFlow openflow:1 f#

Where # is a number between 1 and 80. This will create one of 80
possible flows. You can go confirm they were created on the switch.

Once you’ve done that, use

-  GET

-  Accept: application/xml

-  URL:
   "http://192.168.195.157:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/2/"

To see a full listing of the flows in table 2 (where they will be put).
If you want to see a particular flow, look at

-  URL:
   "http://192.168.195.157:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/2/flow/#"

Where # is 123 + the f# you used. So for example, for f22, your url
would be

-  URL:
   "http://192.168.195.157:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/2/flow/145"

Note: You may have to trim out some of the sections like that contain
bitfields and binary types that are not correctly modeled.

Note: Before attempting to PUT a flow you have created via addMDFlow,
please change its URL and body to, for example, use table 1 instead of
table 2 or another Flow Id, so you don’t collide.

Note: There are several test command providers and the one handling
flows is **OpenflowpluginTestCommandProvider**. Methods, which can be
use as **commands in OSGI-console** have prefix *\_*.

Example Flows
^^^^^^^^^^^^^

Examples for XML for various flow matches, instructions & actions can be
found in following section `here <#odl-ofp-example-flows_overview>`__

End to End Topology
~~~~~~~~~~~~~~~~~~~

Introduction
^^^^^^^^^^^^

The purpose of this page is to walk you through how to see the Topology
Manager working end to end with the openflowplugin using OpenFlow 1.3.

Basically, you will learn how to:

1. Run the Base/Virtualization/Service provider Edition with the new
   openflowplugin: `Running the controller with the new OpenFlow
   Plugin <#odl-ofp-running-controller-with-the-new-of-plugin_top>`__

2. Start mininet to use OF 1.3: `OpenFlow 1.3 Enabled Software Switches
   / Environment <#odl-ofp-test-environment_top>`__

3. Use RESTCONF to see the topology information.

Restconf for Topology
^^^^^^^^^^^^^^^^^^^^^

The REST url for listing all the nodes is:

::

    http://localhost:8080/restconf/operational/network-topology:network-topology/

You will need to set the Accept header:

::

    Accept: application/xml

You will also need to use HTTP Basic Auth with username: admin password:
admin.

Alternately, if you have a node’s id you can address it as

::

    http://localhost:8080/restconf/operational/network-topology:network-topology/topology/<id>

for example

::

    http://localhost:8080/restconf/operational/network-topology:network-topology/topology/flow:1/

How to hit RestConf with Postman
''''''''''''''''''''''''''''''''

Install
`postman <https://chrome.google.com/webstore/detail/postman-rest-client/fdmmgilgnpjigdojojpjoooidkmcomcm?hl=en>`__
for Chrome

In the chrome browser bar enter

::

    chrome://apps/

And click on Postman.

Enter the URL. Click on the Headers button on the far right. Enter the
Accept: header. Click on the Basic Auth Tab at the top and setup the
username and password. Send.

End to End Groups
~~~~~~~~~~~~~~~~~

NOTE
^^^^

Groups are NOT SUPPORTED in current (2.0.0) version of
`openvswitch <http://www.openvswitch.org/download>`__. See

-  http://openvswitch.org/releases/NEWS-2.0.0

-  http://comments.gmane.org/gmane.linux.network.openvswitch.general/3251

For testing group feature please use for example
`CPQD <#odl-ofp-end-to-end-inventory_introduction-introduction>`__
virtual switch.

Instructions
^^^^^^^^^^^^

Learn End to End for Inventory
''''''''''''''''''''''''''''''

`End to End
Inventory <#odl-ofp-end-to-end-inventory_introduction-introduction>`__

Check inventory
'''''''''''''''

Run CPqD with support for OF 1.3 as described in `End to End
Inventory <#odl-ofp-end-to-end-inventory_introduction-introduction>`__

Make sure you see the openflow:1 node come up as described in `End to
End
Inventory <#odl-ofp-end-to-end-inventory_introduction-introduction>`__

Group Strategy
''''''''''''''

Current way to flush a group to switch looks like this:

1. create MD-SAL modeled group and commit it into dataStore using two
   phase commit

2. FRM gets notified and invokes corresponding rpc (addGroup) on
   particular service provider (if suitable provider for given node
   registered)

3. the provider (plugin in this case) transforms MD-SAL modeled group
   into OF-API modeled group

4. OF-API modeled group is then flushed into OFLibrary

5. OFLibrary encodes group into particular version of wire protocol and
   sends it to particular switch

6. check on CPqD if group is installed

Push your Group
'''''''''''''''

-  With PostMan:

   -  Set

      -  Content-Type: application/xml

      -  Accept: application/xml

   -  Use URL:
      "http://<ip-address>:8080/restconf/config/opendaylight-inventory:nodes/node/openflow:1/group/1"

   -  PUT

   -  Use Body:

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <group xmlns="urn:opendaylight:flow:inventory">
        <group-type>group-all</group-type>
        <buckets>
            <bucket>
                <action>
                    <pop-vlan-action/>
                    <order>0</order>
                </action>
                <bucket-id>12</bucket-id>
                <watch_group>14</watch_group>
                <watch_port>1234</watch_port>
            </bucket>
            <bucket>
                <action>
                    <set-field>
                        <ipv4-source>100.1.1.1</ipv4-source>
                    </set-field>
                    <order>0</order>
                </action>
                <action>
                    <set-field>
                        <ipv4-destination>200.71.9.5210</ipv4-destination>
                    </set-field>
                    <order>1</order>
                </action>
                <bucket-id>13</bucket-id>
                <watch_group>14</watch_group>
                <watch_port>1234</watch_port>
            </bucket>
        </buckets>
        <barrier>false</barrier>
        <group-name>Foo</group-name>
        <group-id>1</group-id>
    </group>

    **Note**

    If you want to try a different group id, make sure the URL and the
    body stay in sync. For example, if you wanted to try: group-id 20
    you’d change the URL to
    "http://<ip-address>:8080/restconf/config/opendaylight-inventory:nodes/node/openflow:1/group/20"
    but you would also need to update the <group-id>20</group-id> in the
    body to match.

    **Note**

    <ip-address> :Provide the IP Address of the machine on which the
    controller is running.

Check for your group on the switch
''''''''''''''''''''''''''''''''''

-  See your group on your cpqd switch:

::

    COMMAND: sudo dpctl tcp:127.0.0.1:6000 stats-group

    SENDING:
    stat_req{type="grp", flags="0x0", group="all"}


    RECEIVED:
    stat_repl{type="grp", flags="0x0", stats=[
    {group="1", ref_cnt="0", pkt_cnt="0", byte_cnt="0", cntrs=[{pkt_cnt="0", byte_cnt="0"}, {pkt_cnt="0", byte_cnt="0"}]}]}

Check for your group in the controller config via RESTCONF
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

-  See your configured group in POSTMAN with

   -  URL
      `http://<ip-address>:8080/restconf/config/opendaylight-inventory:nodes/node/openflow:1/group/1 <http://<ip-address>:8080/restconf/config/opendaylight-inventory:nodes/node/openflow:1/group/1>`__

   -  GET

   -  You should no longer need to set Accept

   -  Note: <ip-address> :Provide the IP Address of the machine on which
      the controller is running.

Look for your group stats in the controller operational data via RESTCONF
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

-  See your operational group stats in POSTMAN with

   -  URL
      `http://<ip-address>:8080/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/group/1 <http://<ip-address>:8080/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/group/1>`__

   -  GET

   -  Note: <ip-address> :Provide the IP Address of the machine on which
      the controller is running.

Discovering and testing Group Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently, the openflowplugin has a test-provider that allows you to
push various groups through the system from the OSGI command line. Once
those groups have been pushed through, you can see them as examples and
then use them to see in the config what a particular group example looks
like.

Using addGroup
^^^^^^^^^^^^^^

From the

::

    cd openflowplugin/distribution/base/target/distributions-openflowplugin-base-0.0.1-SNAPSHOT-osgipackage/opendaylight
    ./run.sh

Point your CPqD at the controller as described above.

once you can see your node (probably openflow:1 if you’ve been following
along) in the inventory, at the OSGI command line try running:

::

    addGroup openflow:1

This will install a group in the switch. You can check whether the group
is installed or not.

Once you’ve done that, use

-  GET

-  Accept: application/xml

-  URL:
   "http://<ip-address>:8080/restconf/config/opendaylight-inventory:nodes/node/openflow:1/group/1"

   -  Note: <ip-address> :Provide the IP Address of the machine on which
      the controller is running.

    **Note**

    Before attempting to PUT a group you have created via addGroup,
    please change its URL and body to, for example, use group 1 instead
    of group 2 or another Group Id, so that they don’t collide.

    **Note**

    There are several test command providers and the one handling groups
    is OpenflowpluginGroupTestCommandProvider. Methods, which can be use
    as commands in OSGI-console have prefix *\_*.

Example Group
^^^^^^^^^^^^^

Examples for XML for various Group Types can be found in the
test-scripts bundle of the plugin code with names g1.xml, g2.xml and
g3.xml.

End to End Meters
~~~~~~~~~~~~~~~~~

Instructions
^^^^^^^^^^^^

Learn End to End for Inventory
''''''''''''''''''''''''''''''

-  `End to End
   Inventory <#odl-ofp-end-to-end-inventory_introduction-introduction>`__

Check inventory
'''''''''''''''

-  Run mininet with support for OF 1.3 as described in `End to End
   Inventory <#odl-ofp-end-to-end-inventory_introduction-introduction>`__

-  Make sure you see the openflow:1 node come up as described in `End to
   End
   Inventory <#odl-ofp-end-to-end-inventory_introduction-introduction>`__

Meter Strategy
''''''''''''''

Current way to flush a meter to switch looks like this:

1. create MD-SAL modeled flow and commit it into dataStore using two
   phase commit

2. FRM gets notified and invokes corresponding rpc (addMeter) on
   particular service provider (if suitable provider for given node
   registered)

3. the provider (plugin in this case) transforms MD-SAL modeled meter
   into OF-API modeled meter

4. OF-API modeled meter is then flushed into OFLibrary

5. OFLibrary encodes meter into particular version of wire protocol and
   sends it to particular switch

6. check on mininet side if meter is installed

Push your Meter
'''''''''''''''

-  Using PostMan:

   -  Set Request Headers

      -  Content-Type: application/xml

      -  Accept: application/xml

   -  Use URL:
      "http://:8080/restconf/config/opendaylight-inventory:nodes/node/openflow:1/meter/1"

   -  Method:PUT

   -  Request Body:

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <meter xmlns="urn:opendaylight:flow:inventory">
        <container-name>abcd</container-name>
        <flags>meter-burst</flags>
        <meter-band-headers>
            <meter-band-header>
                <band-burst-size>444</band-burst-size>
                <band-id>0</band-id>
                <band-rate>234</band-rate>
                <dscp-remark-burst-size>5</dscp-remark-burst-size>
                <dscp-remark-rate>12</dscp-remark-rate>
                <prec_level>1</prec_level>
                <meter-band-types>
                    <flags>ofpmbt-dscp-remark</flags>
                </meter-band-types>
            </meter-band-header>
        </meter-band-headers>
        <meter-id>1</meter-id>
        <meter-name>Foo</meter-name>
    </meter>

    **Note**

    If you want to try a different meter id, make sure the URL and the
    body stay in sync. For example, if you wanted to try: meter-id 20
    you’d change the URL to
    "http://:8080/restconf/config/opendaylight-inventory:nodes/node/openflow:1/meter/20"
    but you would also need to update the 20 in the body to match.

    **Note**

    :Provide the IP Address of the machine on which the controller is
    running.

Check for your meter on the switch
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  See your meter on your CPqD switch:

::

    COMMAND: $ sudo dpctl tcp:127.0.0.1:6000 meter-config

    SENDING:
    stat_req{type="mconf", flags="0x0"{meter_id= ffffffff"}


    RECEIVED:
    stat_repl{type="mconf", flags="0x0", stats=[{meter= c"", flags="4", bands=[{type = dscp_remark, rate="12", burst_size="5", prec_level="1"}]}]}

Check for your meter in the controller config via RESTCONF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  See your configured flow in POSTMAN with

   -  URL
      "http://:8080/restconf/config/opendaylight-inventory:nodes/node/openflow:1/meter/1"

   -  Method: GET

   -  You should no longer need to set Request Headers for Accept

   -  Note: :Provide the IP Address of the machine on which the
      controller is running.

Look for your meter stats in the controller operational data via RESTCONF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  See your operational meter stats in POSTMAN with

   -  URL
      "http://:8080/restconfig/operational/opendaylight-inventory:nodes/node/openflow:1/meter/1"

   -  Method: GET

   -  Note: :Provide the IP Address of the machine on which the
      controller is running.

Discovering and testing Meter Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Currently, the openflowplugin has a test-provider that allows you to
push various meters through the system from the OSGI command line. Once
those meters have been pushed through, you can see them as examples and
then use them to see in the config what a particular meter example looks
like.

Using addMeter
''''''''''''''

From the

::

    cd openflowplugin/distribution/base/target/distributions-openflowplugin-base-0.0.1-SNAPSHOT-osgipackage/opendaylight
    ./run.sh

Point your CPqD at the controller as described above.

Once you can see your CPqD connected to the controller, at the OSGI
command line try running:

::

    addMeter openflow:1

Once you’ve done that, use

-  GET

-  Accept: application/xml

-  URL:
   "http://:8080/restconf/config/opendaylight-inventory:nodes/node/openflow:1/meter/12"

   -  Note: :Provide the IP Address of the machine on which the
      controller is running.

    **Note**

    Before attempting to PUT a meter you have created via addMeter,
    please change its URL and body to, for example, use meter 1 instead
    of meter 2 or another Meter Id, so you don’t collide.

    **Note**

    There are several test command providers and the one handling Meter
    is **OpenflowpluginMeterTestCommandProvider**. Methods, which can be
    used as **commands in OSGI-console** have prefix *\_*. Examples:
    addMeter, modifyMeter and removeMeter.

Example Meter
^^^^^^^^^^^^^

Examples for XML for various Meter Types can be found in the
test-scripts bundle of the plugin code with names m1.xml, m2.xml and
m3.xml.

Statistics
~~~~~~~~~~

Overview
^^^^^^^^

This page contains high level detail about the statistics collection
mechanism in new OpenFlow plugin.

Statistics collection in new OpenFlow plugin
''''''''''''''''''''''''''''''''''''''''''''

New OpenFlow plugin collects following statistics from OpenFlow enabled
node(switch):

1.  Individual Flow Statistics

2.  Aggregate Flow Statistics

3.  Flow Table Statistics

4.  Port Statistics

5.  Group Description

6.  Group Statistics

7.  Meter Configuration

8.  Meter Statistics

9.  Queue Statistics

10. Node Description

11. Flow Table Features

12. Port Description

13. Group Features

14. Meter Features

At a high level statistics collection mechanism is divided into
following three parts

1. Statistics related `YANG models, service APIs and notification
   interfaces <https://git.opendaylight.org/gerrit/gitweb?p=controller.git;a=tree;f=opendaylight/md-sal/model/model-flow-statistics;h=3488133625ccf18d023bc59aa35c38e922b17d8d;hb=HEAD>`__
   are defined in the MD-SAL.

2. Service APIs (RPCs) defined in yang models are implemented by
   OpenFlow plugin. Notification interfaces are wired up by OpenFlow
   plugin to MD-SAL.

3. Statistics Manager Module: This module use service APIs implemented
   by OpenFlow plugin to send statistics requests to all the connected
   OpenFlow enabled nodes. Module also implements notification
   interfaces to receive statistics response from nodes. Once it
   receives statistics response, it augment all the statistics data to
   the relevant element of the node (like node-connector, flow,
   table,group, meter) and store it in MD-SAL operational data store.

Details of statistics collection
''''''''''''''''''''''''''''''''

-  Current implementation collects above mentioned statistics (except
   10-14) at a periodic interval of 15 seconds.

-  Statistics mentioned in 10 to 14 are only fetched when any node
   connects to the controller because these statistics are just static
   details about the respective elements.

-  Whenever any new element is added to node (like flow, group, meter,
   queue) it sends statistics request immediately to fetch the latest
   statistics and store it in the operational data store.

-  Whenever any element is deleted from the node, it immediately remove
   the relevant statistics from operational data store.

-  Statistics data are augmented to their respective element stored in
   the configuration data store. E.g Controller installed flows are
   stored in configuration data store. Whenever Statistics Manager
   receive statistics data related to these flow, it search the
   corresponding flow in the configuration data store and augment
   statistics in the corresponding location in operational data store.
   Similar approach is used for other elements of the node.

-  Statistics Manager stores flow statistics as an unaccounted flow
   statistics in operational data store if there is no corresponding
   flow exist in configuration data store. ID format of unaccounted flow
   statistics is as follows - [#UF$TABLE\*\*Unaccounted-flow-count - e.g
   #UF$TABLE\*2\*1].

-  All the unaccounted flows will be cleaned up periodically after every
   two cycle of flow statistics collection, given that there is no
   update for these flows in the last two cycles.

-  Statistics Manager only entertains statistics response for the
   request sent by itself. User can write its own statistics collector
   using the statistics service APIs and notification defined in yang
   models, it won’t effect the functioning of Statistics Manager.

-  OpenFlow 1.0 don’t have concept of Meter and Group, so Statistics
   Manager don’t send any group & meter related statistics request to
   OpenFlow 1.0 enabled switch.

RESTCONF Uris to access statistics of various node elements
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

-  Aggregate Flow Statistics & Flow Table Statistics

::

    GET  http://<controller-ip>:8080/restconf/operational/opendaylight-inventory:nodes/node/{node-id}/table/{table-id}

-  Individual Flow Statistics from specific table

::

    GET  http://<controller-ip>:8080/restconf/operational/opendaylight-inventory:nodes/node/{node-id}/table/{table-id}/flow/{flow-id}

-  Group Features & Meter Features Statistics

::

    GET  http://<controller-ip>:8080/restconf/operational/opendaylight-inventory:nodes/node/{node-id}

-  Group Description & Group Statistics

::

    GET  http://<controller-ip>:8080/restconf/operational/opendaylight-inventory:nodes/node/{node-id}/group/{group-id}

-  Meter Configuration & Meter Statistics

::

    GET  http://<controller-ip>:8080/restconf/operational/opendaylight-inventory:nodes/node/{node-id}/meter/{meter-id}

-  Node Connector Statistics

::

    GET  http://<controller-ip>:8080/restconf/operational/opendaylight-inventory:nodes/node/{node-id}/node-connector/{node-connector-id}

-  Queue Statistics

::

    GET  http://<controller-ip>:8080/restconf/operational/opendaylight-inventory:nodes/node/{node-id}/node-connector/{node-connector-id}/queue/{queue-id}

Bugs
''''

For more details and queuries, please send mail to
openflowplugin-dev@lists.opendaylight.org or avishnoi@in.ibm.com If you
want to report any bug in statistics collection, please use
`bugzilla <https://bugs.opendaylight.org>`__.

Web / Graphical Interface
-------------------------

In the Hydrogen & Helium release, the current Web UI does not support
the new OpenFlow 1.3 constructs such as groups, meters, new fields in
the flows, multiple flow tables, etc.

Command Line Interface
----------------------

The following is not exactly CLI - just a set of test commands which can
be executed on the OSGI console testing various features in OpenFlow 1.3
spec.

-  `OSGI Console Test Provider Commands:
   Flows <#odl-ofp-test-provider-flows_test-provider>`__

-  `OSGI Console Test Provider Commands:
   Groups <#odl-ofp-test-provider-groups_test-provider>`__

-  `OSGI Console Test Provider Commands:
   Meters <#odl-ofp-test-provider-meters_test-provider>`__

-  `OSGI Console Test Provider Commands: Topology
   Events <#odl-ofp-test-provider-topoogy_test-provider>`__

Flows : Test Provider
~~~~~~~~~~~~~~~~~~~~~

Currently, the openflowplugin has a test-provider that allows you to
push various flows through the system from the OSGI command line. Once
those flows have been pushed through, you can see them as examples and
then use them to see in the config what a particular flow example looks
like.

AddFlow : addMDFlow
^^^^^^^^^^^^^^^^^^^

Run the controller by executing:

::

    cd openflowplugin/distribution/base/target/distributions-openflowplugin-base-0.0.1-SNAPSHOT-osgipackage/opendaylight
    ./run.sh

Point your mininet to the controller by giving the parameters
--controller=remote,ip=.

Once you see your node (probably openflow:1 if you’ve been following
along) in the inventory, at the OSGI command line try running:

::

    addMDFlow openflow:1 f#

Where # is a number between 1 and 80 and openflow:1 is the of the
switch. This will create one of 80 possible flows. You can confirm that
they were created on the switch.

RemoveFlow : removeMDFlow
^^^^^^^^^^^^^^^^^^^^^^^^^

Similar to addMDFlow, from the controller OSGi prompt, while your switch
is connected to the controller, try running:

::

    removeMDFlow openflow:1 f#

where # is a number between 1 and 80 and openflow:1 is the of the
switch. The flow to be deleted should have same flowid and Nodeid as
used for flow add.

ModifyFlow : modifyMDFlow
^^^^^^^^^^^^^^^^^^^^^^^^^

Similar to addMDFlow, from the controller OSGi prompt, while your switch
is connected to the controller, try running:

::

    modifyMDFlow openflow:1 f#

where # is a number between 1 and 80 and openflow:1 is the of the
switch. The flow to be deleted should have same flowid and Nodeid as
used for flow add.

Group : Test Provider
~~~~~~~~~~~~~~~~~~~~~

Currently, the openflowplugin has a test-provider that allows you to
push various flows through the system from the OSGI command line. Once
those flows have been pushed through, you can see them as examples and
then use them to see in the config what a particular flow example looks
like.

AddGroup : addGroup
^^^^^^^^^^^^^^^^^^^

Run the controller by executing:

::

    cd openflowplugin/distribution/base/target/distributions-openflowplugin-base-0.0.1-SNAPSHOT-osgipackage/opendaylight
    ./run.sh

Point your mininet to the controller by giving the parameters
--controller=remote,ip=.

Once you see your node (probably openflow:1 if you’ve been following
along) in the inventory, at the OSGI command line try running:

::

    addGroup openflow:1 a# g#

Where # is a number between 1 and 4 for grouptype(g#) and 1 and 28 for
actiontype(a#). You can confirm that they were created on the switch.

RemoveGroup : removeGroup
^^^^^^^^^^^^^^^^^^^^^^^^^

Run the controller by executing:

::

    cd openflowplugin/distribution/base/target/distributions-openflowplugin-base-0.0.1-SNAPSHOT-osgipackage/opendaylight
    ./run.sh

Point your mininet at the controller as described above.

Once you see your node (probably openflow:1 if you’ve been following
along) in the inventory, at the OSGI command line try running:

::

    removeGroup openflow:1 a# g#

Where # is a number between 1 and 4 for grouptype(g#) and 1 and 28 for
actiontype(a#). GroupId should be same as that used for adding the flow.
You can confirm that it was removed from the switch.

ModifyGroup : modifyGroup
^^^^^^^^^^^^^^^^^^^^^^^^^

Run the controller by executing:

::

    cd openflowplugin/distribution/base/target/distributions-openflowplugin-base-0.0.1-SNAPSHOT-osgipackage/opendaylight
    ./run.sh

Point your mininet at the controller as described above.

Once you see your node (probably openflow:1 if you’ve been following
along) in the inventory, at the OSGI command line try running:

::

    modifyGroup openflow:1 a# g#

Where # is a number between 1 and 4 for grouptype(g#) and 1 and 28 for
actiontype(a#). GroupId should be same as that used for adding the flow.
You can confirm that it was modified on the switch.

Meters : Test Provider
~~~~~~~~~~~~~~~~~~~~~~

Currently, the openflowplugin has a test-provider that allows you to
push various flows through the system from the OSGI command line. Once
those flows have been pushed through, you can see them as examples and
then use them to see in the config what a particular flow example looks
like.

AddMeter : addMeter
^^^^^^^^^^^^^^^^^^^

Run the controller by executing:

::

    cd openflowplugin/distribution/base/target/distributions-openflowplugin-base-0.0.1-SNAPSHOT-osgipackage/opendaylight
    ./run.sh

Point your mininet to the controller by giving the parameters
--controller=remote,ip=.

Once you see your node (probably openflow:1 if you’ve been following
along) in the inventory, at the OSGI command line try running:

::

    addMeter openflow:1

You can now confirm that meter has been created on the switch.

RemoveMeter : removeMeter
^^^^^^^^^^^^^^^^^^^^^^^^^

Run the controller by executing:

::

    cd openflowplugin/distribution/base/target/distributions-openflowplugin-base-0.0.1-SNAPSHOT-osgipackage/opendaylight
    ./run.sh

Point your mininet to the controller by giving the parameters
--controller=remote,ip=.

Once you see your node (probably openflow:1 if you’ve been following
along) in the inventory, at the OSGI command line try running:

::

    removeMeter openflow:1

The CLI takes care of using the same meterId and nodeId as used for
meter add. You can confirm that it was removed from the switch.

ModifyMeter : modifyMeter
^^^^^^^^^^^^^^^^^^^^^^^^^

Run the controller by executing:

::

    cd openflowplugin/distribution/base/target/distributions-openflowplugin-base-0.0.1-SNAPSHOT-osgipackage/opendaylight
    ./run.sh

Point your mininet to the controller by giving the parameters
--controller=remote,ip=.

Once you see your node (probably openflow:1 if you’ve been following
along) in the inventory, at the OSGI command line try running:

::

    modifyMeter openflow:1

The CLI takes care of using the same meterId and nodeId as used for
meter add. You can confirm that it was modified on the switch.

Topology : Notification
~~~~~~~~~~~~~~~~~~~~~~~

Currently, the openflowplugin has a test-provider that allows you to get
notifications for the topology related events like Link-Discovered ,
Link-Removed events.

Link Discovered Event : Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Run the controller by executing:

::

    cd openflowplugin/distribution/base/target/distributions-openflowplugin-base-0.0.1-SNAPSHOT-osgipackage/opendaylight
    ./run.sh

Point your mininet to the controller by giving the parameters
--controller=remote,ip=. Once the controller is connected to the switch,
Link-Discovered event can be tested by initially configuring the
specific flows on the switch. For Link Discovered event either
table-miss flow or LLDP ether-type flow can be configured.

Configuring Table-Miss flow using OpenflowpluginTestCommandProvider

::

    addMDFlow Openflow:1 fTM

as per this
OpenDaylight\_OpenFlow\_Plugin:Test\_Provider#Flows\_:\_Test\_Provider[link].
*fTM* is the table-miss scenario here.

Once the table-miss flow is configured through above command, we can see
the Link-Discovered event in the debug logs on the controller console.

Configuring LLDP ether-type flow using OpenflowpluginTestCommandProvider

::

    addMDFlow Openflow:1 0(table-id) f81

You can confirm that they were created on the switch.

Once the LLDP ether-type flow is configured through above command, we
can see the Link-Discovered event in the debug logs on the controller
console.

Link Removed Event : Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Having configured either table-miss or lldp ether-type flow on switch,
once the switch is disconnected we see the Link-Removed event

Programmatic Interface
----------------------

The API is documented in the model documentation under the section
OpenFlow Services at:

-  `Models Documentation (OpenFlow Services
   Section) <https://wiki.opendaylight.org/view/OpenDaylight_Controller:Config:Model_Reference>`__

Example flows
-------------

Overview
~~~~~~~~

The flow examples on this page are tested to work with OVS.

Use, for example, POSTMAN with the following parameters:

::

    PUT http://<ctrl-addr>:8080/restconf/config/opendaylight-inventory:nodes/node/<Node-id>/table/<Table-#>/flow/<Flow-#>

    - Accept: application/xml
    - Content-Type: application/xml

For example:

::

    PUT http://localhost:8080/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/2/flow/127

Make sure that the Table-# and Flow-# in the URL and in the XML match.

The format of the flow-programming XML is determined by by the grouping
*flow* in the opendaylight-flow-types yang model: MISSING LINK.

Match Examples
~~~~~~~~~~~~~~

The format of the XML that describes OpenFlow matches is determined by
the opendaylight-match-types yang model: .

The RESTCONF documentation for the match-types yang model can be found
at
`opendaylight-match-types.html <https://jenkins.opendaylight.org/controller/job/controller-merge/lastSuccessfulBuild/artifact/opendaylight/md-sal/model/model-flow-base/target/site/models/opendaylight-match-types.html>`__

IPv4 Dest Address
^^^^^^^^^^^^^^^^^

-  Flow=124, Table=2, Priority=2,
   Instructions=\\{Apply\_Actions={dec\_nw\_ttl}},
   match=\\{ipv4\_destination\_address=10.0.1.1/24}

-  Note that ethernet-type MUST be 2048 (0x800)

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <table_id>2</table_id>
        <id>124</id>
        <cookie_mask>255</cookie_mask>
        <installHw>false</installHw>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
            </ethernet-match>
            <ipv4-destination>10.0.1.1/24</ipv4-destination>
        </match>
        <hard-timeout>12</hard-timeout>
        <cookie>1</cookie>
        <idle-timeout>34</idle-timeout>
        <flow-name>FooXf1</flow-name>
        <priority>2</priority>
        <barrier>false</barrier>
    </flow>

Ethernet Src Address
^^^^^^^^^^^^^^^^^^^^

-  Flow=126, Table=2, Priority=2,
   Instructions=\\{Apply\_Actions={drop}},
   match=\\{ethernet-source=00:00:00:00:00:01}

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <drop-action/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <table_id>2</table_id>
        <id>126</id>
        <cookie_mask>255</cookie_mask>
        <installHw>false</installHw>
        <match>
            <ethernet-match>
                <ethernet-source>
                    <address>00:00:00:00:00:01</address>
                </ethernet-source>
            </ethernet-match>
        </match>
        <hard-timeout>12</hard-timeout>
        <cookie>3</cookie>
        <idle-timeout>34</idle-timeout>
        <flow-name>FooXf3</flow-name>
        <priority>2</priority>
        <barrier>false</barrier>
    </flow>

Ethernet Src & Dest Addresses, Ethernet Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Flow=127, Table=2, Priority=2,
   Instructions=\\{Apply\_Actions={drop}},
   match=\\{ethernet-source=00:00:00:00:23:ae,
   ethernet-destination=ff:ff:ff:ff:ff:ff, ethernet-type=45}

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-mpls-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <table_id>2</table_id>
        <id>127</id>
        <cookie_mask>255</cookie_mask>
        <installHw>false</installHw>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>45</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>ff:ff:ff:ff:ff:ff</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:00:23:ae</address>
                </ethernet-source>
            </ethernet-match>
        </match>
        <hard-timeout>12</hard-timeout>
        <cookie>4</cookie>
        <idle-timeout>34</idle-timeout>
        <flow-name>FooXf4</flow-name>
        <priority>2</priority>
        <barrier>false</barrier>
    </flow>

Ethernet Src & Dest Addresses, IPv4 Src & Dest Addresses, Input Port
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Note that ethernet-type MUST be 34887 (0x8847)

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-mpls-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <table_id>2</table_id>
        <id>128</id>
        <cookie_mask>255</cookie_mask>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34887</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>ff:ff:ff:ff:ff:ff</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:00:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <ipv4-source>10.1.2.3/24</ipv4-source>
            <ipv4-destination>20.4.5.6/16</ipv4-destination>
            <in-port>0</in-port>
        </match>
        <hard-timeout>12</hard-timeout>
        <cookie>5</cookie>
        <idle-timeout>34</idle-timeout>
        <flow-name>FooXf5</flow-name>
        <priority>2</priority>
        <barrier>false</barrier>
    </flow>

Ethernet Src & Dest Addresses, IPv4 Src & Dest Addresses, IP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Protocol #, IP DSCP, IP ECN, Input Port

-  Note that ethernet-type MUST be 2048 (0x800)

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <table_id>2</table_id>
        <id>130</id>
        <cookie_mask>255</cookie_mask>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>ff:ff:ff:ff:ff:aa</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:11:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <ipv4-source>10.1.2.3/24</ipv4-source>
            <ipv4-destination>20.4.5.6/16</ipv4-destination>
            <ip-match>
                <ip-protocol>56</ip-protocol>
                <ip-dscp>15</ip-dscp>
                <ip-ecn>1</ip-ecn>
            </ip-match>
            <in-port>0</in-port>
        </match>
        <hard-timeout>12000</hard-timeout>
        <cookie>7</cookie>
        <idle-timeout>12000</idle-timeout>
        <flow-name>FooXf7</flow-name>
        <priority>2</priority>
        <barrier>false</barrier>
    </flow>

Ethernet Src & Dest Addresses, IPv4 Src & Dest Addresses, TCP Src &
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dest Ports, IP DSCP, IP ECN, Input Port

-  Note that ethernet-type MUST be 2048 (0x800)

-  Note that IP Protocol Type MUST be 6

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <table_id>2</table_id>
        <id>131</id>
        <cookie_mask>255</cookie_mask>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>ff:ff:29:01:19:61</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:11:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <ipv4-source>17.1.2.3/8</ipv4-source>
            <ipv4-destination>172.168.5.6/16</ipv4-destination>
            <ip-match>
                <ip-protocol>6</ip-protocol>
                <ip-dscp>2</ip-dscp>
                <ip-ecn>2</ip-ecn>
            </ip-match>
            <tcp-source-port>25364</tcp-source-port>
            <tcp-destination-port>8080</tcp-destination-port>
            <in-port>0</in-port>
        </match>
        <hard-timeout>1200</hard-timeout>
        <cookie>8</cookie>
        <idle-timeout>3400</idle-timeout>
        <flow-name>FooXf8</flow-name>
        <priority>2</priority>
        <barrier>false</barrier>
    </flow>

Ethernet Src & Dest Addresses, IPv4 Src & Dest Addresses, UDP Src &
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dest Ports, IP DSCP, IP ECN, Input Port

-  Note that ethernet-type MUST be 2048 (0x800)

-  Note that IP Protocol Type MUST be 17

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <table_id>2</table_id>
        <id>132</id>
        <cookie_mask>255</cookie_mask>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>20:14:29:01:19:61</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:11:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <ipv4-source>19.1.2.3/10</ipv4-source>
            <ipv4-destination>172.168.5.6/18</ipv4-destination>
            <ip-match>
                <ip-protocol>17</ip-protocol>
                <ip-dscp>8</ip-dscp>
                <ip-ecn>3</ip-ecn>
            </ip-match>
            <udp-source-port>25364</udp-source-port>
            <udp-destination-port>8080</udp-destination-port>
            <in-port>0</in-port>
        </match>
        <hard-timeout>1200</hard-timeout>
        <cookie>9</cookie>
        <idle-timeout>3400</idle-timeout>
        <flow-name>FooXf9</flow-name>
        <priority>2</priority>
        <barrier>false</barrier>

Ethernet Src & Dest Addresses, IPv4 Src & Dest Addresses, ICMPv4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Type & Code, IP DSCP, IP ECN, Input Port

-  Note that ethernet-type MUST be 2048 (0x800)

-  Note that IP Protocol Type MUST be 1

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <table_id>2</table_id>
        <id>134</id>
        <cookie_mask>255</cookie_mask>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>ff:ff:29:01:19:61</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:11:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <ipv4-source>17.1.2.3/8</ipv4-source>
            <ipv4-destination>172.168.5.6/16</ipv4-destination>
            <ip-match>
                <ip-protocol>1</ip-protocol>
                <ip-dscp>27</ip-dscp>
                <ip-ecn>3</ip-ecn>
            </ip-match>
            <icmpv4-match>
                <icmpv4-type>6</icmpv4-type>
                <icmpv4-code>3</icmpv4-code>
            </icmpv4-match>
            <in-port>0</in-port>
        </match>
        <hard-timeout>1200</hard-timeout>
        <cookie>11</cookie>
        <idle-timeout>3400</idle-timeout>
        <flow-name>FooXf11</flow-name>
        <priority>2</priority>
    </flow>

Ethernet Src & Dest Addresses, ARP Operation, ARP Src & Target
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transport Addresses, ARP Src & Target Hw Addresses

-  Note that ethernet-type MUST be 2054 (0x806)

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                    <action>
                        <order>1</order>
                        <dec-mpls-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <table_id>2</table_id>
        <id>137</id>
        <cookie_mask>255</cookie_mask>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2054</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>ff:ff:ff:ff:FF:ff</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:FC:01:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <arp-op>1</arp-op>
            <arp-source-transport-address>192.168.4.1</arp-source-transport-address>
            <arp-target-transport-address>10.21.22.23</arp-target-transport-address>
            <arp-source-hardware-address>
                <address>12:34:56:78:98:AB</address>
            </arp-source-hardware-address>
            <arp-target-hardware-address>
                <address>FE:DC:BA:98:76:54</address>
            </arp-target-hardware-address>
        </match>
        <hard-timeout>12</hard-timeout>
        <cookie>14</cookie>
        <idle-timeout>34</idle-timeout>
        <flow-name>FooXf14</flow-name>
        <priority>2</priority>
        <barrier>false</barrier>

Ethernet Src & Dest Addresses, Ethernet Type, VLAN ID, VLAN PCP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <table_id>2</table_id>
        <id>138</id>
        <cookie_mask>255</cookie_mask>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>ff:ff:29:01:19:61</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:11:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <vlan-match>
                <vlan-id>
                    <vlan-id>78</vlan-id>
                    <vlan-id-present>true</vlan-id-present>
                </vlan-id>
                <vlan-pcp>3</vlan-pcp>
          </vlan-match>
        </match>
        <hard-timeout>1200</hard-timeout>
        <cookie>15</cookie>
        <idle-timeout>3400</idle-timeout>
        <flow-name>FooXf15</flow-name>
        <priority>2</priority>
        <barrier>false</barrier>
    </flow>

Ethernet Src & Dest Addresses, MPLS Label, MPLS TC, MPLS BoS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <flow-name>FooXf17</flow-name>
        <id>140</id>
        <cookie_mask>255</cookie_mask>
        <cookie>17</cookie>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <priority>2</priority>
        <table_id>2</table_id>
        <strict>false</strict>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34887</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>ff:ff:29:01:19:61</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:11:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <protocol-match-fields>
                <mpls-label>567</mpls-label>
                <mpls-tc>3</mpls-tc>
                <mpls-bos>1</mpls-bos>
            </protocol-match-fields>
        </match>
    </flow>

IPv6 Src & Dest Addresses
^^^^^^^^^^^^^^^^^^^^^^^^^

-  Note that ethernet-type MUST be 34525

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf18</flow-name>
        <id>141</id>
        <cookie_mask>255</cookie_mask>
        <cookie>18</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34525</type>
                </ethernet-type>
            </ethernet-match>
            <ipv6-source>fe80::2acf:e9ff:fe21:6431/128</ipv6-source>
            <ipv6-destination>aabb:1234:2acf:e9ff::fe21:6431/64</ipv6-destination>
        </match>
    </flow>

Metadata
^^^^^^^^

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf19</flow-name>
        <id>142</id>
        <cookie_mask>255</cookie_mask>
        <cookie>19</cookie>
        <table_id>2</table_id>
        <priority>1</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <metadata>
                <metadata>12345</metadata>
            </metadata>
        </match>
    </flow>

Metadata, Metadata Mask
^^^^^^^^^^^^^^^^^^^^^^^

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf20</flow-name>
        <id>143</id>
        <cookie_mask>255</cookie_mask>
        <cookie>20</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <metadata>
                <metadata>12345</metadata>
                <metadata-mask>//FF</metadata-mask>
            </metadata>
        </match>
    </flow>

IPv6 Src & Dest Addresses, Metadata, IP DSCP, IP ECN, UDP Src & Dest Ports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Note that ethernet-type MUST be 34525

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf21</flow-name>
        <id>144</id>
        <cookie_mask>255</cookie_mask>
        <cookie>21</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34525</type>
                </ethernet-type>
            </ethernet-match>
            <ipv6-source>1234:5678:9ABC:DEF0:FDCD:A987:6543:210F/76</ipv6-source>
            <ipv6-destination>fe80::2acf:e9ff:fe21:6431/128</ipv6-destination>
            <metadata>
                <metadata>12345</metadata>
            </metadata>
            <ip-match>
                <ip-protocol>17</ip-protocol>
                <ip-dscp>8</ip-dscp>
                <ip-ecn>3</ip-ecn>
            </ip-match>
            <udp-source-port>25364</udp-source-port>
            <udp-destination-port>8080</udp-destination-port>
        </match>
    </flow>

IPv6 Src & Dest Addresses, Metadata, IP DSCP, IP ECN, TCP Src & Dest Ports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Note that ethernet-type MUST be 34525

-  Note that IP Protocol MUST be 6

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf22</flow-name>
        <id>145</id>
        <cookie_mask>255</cookie_mask>
        <cookie>22</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34525</type>
                </ethernet-type>
            </ethernet-match>
            <ipv6-source>1234:5678:9ABC:DEF0:FDCD:A987:6543:210F/76</ipv6-source>
            <ipv6-destination>fe80:2acf:e9ff:fe21::6431/94</ipv6-destination>
            <metadata>
                <metadata>12345</metadata>
            </metadata>
            <ip-match>
                <ip-protocol>6</ip-protocol>
                <ip-dscp>60</ip-dscp>
                <ip-ecn>3</ip-ecn>
            </ip-match>
            <tcp-source-port>183</tcp-source-port>
            <tcp-destination-port>8080</tcp-destination-port>
        </match>
    </flow>

IPv6 Src & Dest Addresses, Metadata, IP DSCP, IP ECN, TCP Src & Dest Ports, IPv6 Label
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Note that ethernet-type MUST be 34525

-  Note that IP Protocol MUST be 6

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf23</flow-name>
        <id>146</id>
        <cookie_mask>255</cookie_mask>
        <cookie>23</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34525</type>
                </ethernet-type>
            </ethernet-match>
            <ipv6-source>1234:5678:9ABC:DEF0:FDCD:A987:6543:210F/76</ipv6-source>
            <ipv6-destination>fe80:2acf:e9ff:fe21::6431/94</ipv6-destination>
            <metadata>
                <metadata>12345</metadata>
            </metadata>
            <ipv6-label>
                <ipv6-flabel>33</ipv6-flabel>
            </ipv6-label>
            <ip-match>
                <ip-protocol>6</ip-protocol>
                <ip-dscp>60</ip-dscp>
                <ip-ecn>3</ip-ecn>
            </ip-match>
            <tcp-source-port>183</tcp-source-port>
            <tcp-destination-port>8080</tcp-destination-port>
        </match>
    </flow>

Tunnel ID
^^^^^^^^^

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf24</flow-name>
        <id>147</id>
        <cookie_mask>255</cookie_mask>
        <cookie>24</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <tunnel>
                <tunnel-id>2591</tunnel-id>
            </tunnel>
        </match>
    </flow>

IPv6 Src & Dest Addresses, Metadata, IP DSCP, IP ECN, ICMPv6 Type & Code, IPv6 Label
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Note that ethernet-type MUST be 34525

-  Note that IP Protocol MUST be 58

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf25</flow-name>
        <id>148</id>
        <cookie_mask>255</cookie_mask>
        <cookie>25</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34525</type>
                </ethernet-type>
            </ethernet-match>
            <ipv6-source>1234:5678:9ABC:DEF0:FDCD:A987:6543:210F/76</ipv6-source>
            <ipv6-destination>fe80:2acf:e9ff:fe21::6431/94</ipv6-destination>
            <metadata>
                <metadata>12345</metadata>
            </metadata>
            <ipv6-label>
                <ipv6-flabel>33</ipv6-flabel>
            </ipv6-label>
            <ip-match>
                <ip-protocol>58</ip-protocol>
                <ip-dscp>60</ip-dscp>
                <ip-ecn>3</ip-ecn>
            </ip-match>
            <icmpv6-match>
                <icmpv6-type>6</icmpv6-type>
                <icmpv6-code>3</icmpv6-code>
            </icmpv6-match>
        </match>
    </flow>

IPv6 Src & Dest Addresses, Metadata, IP DSCP, IP ECN, TCP Src & Dst Ports, IPv6 Label, IPv6 Ext Header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Note that ethernet-type MUST be 34525

-  Note that IP Protocol MUST be 58

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf27</flow-name>
        <id>150</id>
        <cookie_mask>255</cookie_mask>
        <cookie>27</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <dec-nw-ttl/>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34525</type>
                </ethernet-type>
            </ethernet-match>
            <ipv6-source>1234:5678:9ABC:DEF0:FDCD:A987:6543:210F/76</ipv6-source>
            <ipv6-destination>fe80:2acf:e9ff:fe21::6431/94</ipv6-destination>
            <metadata>
                <metadata>12345</metadata>
            </metadata>
            <ipv6-label>
                <ipv6-flabel>33</ipv6-flabel>
            </ipv6-label>
            <ipv6-ext-header>
                <ipv6-exthdr>0</ipv6-exthdr>
            </ipv6-ext-header>
            <ip-match>
                <ip-protocol>6</ip-protocol>
                <ip-dscp>60</ip-dscp>
                <ip-ecn>3</ip-ecn>
            </ip-match>
            <tcp-source-port>183</tcp-source-port>
            <tcp-destination-port>8080</tcp-destination-port>
        </match>
    </flow>

Actions
~~~~~~~

The format of the XML that describes OpenFlow actions is determined by
the opendaylight-action-types yang model: .

The RESTCONF documentation for the match-types yang model can be found
at
`opendaylight-action-types.html <https://jenkins.opendaylight.org/controller/job/controller-merge/lastSuccessfulBuild/artifact/opendaylight/md-sal/model/model-flow-base/target/site/models/opendaylight-action-types.html>`__

Apply Actions
^^^^^^^^^^^^^

Output to TABLE
'''''''''''''''

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf101</flow-name>
        <id>256</id>
        <cookie_mask>255</cookie_mask>
        <cookie>101</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <output-action>
                            <output-node-connector>TABLE</output-node-connector>
                            <max-length>60</max-length>
                        </output-action>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34525</type>
                </ethernet-type>
            </ethernet-match>
            <ipv6-source>1234:5678:9ABC:DEF0:FDCD:A987:6543:210F/76</ipv6-source>
            <ipv6-destination>fe80:2acf:e9ff:fe21::6431/94</ipv6-destination>
            <metadata>
                <metadata>12345</metadata>
            </metadata>
            <ip-match>
                <ip-protocol>6</ip-protocol>
                <ip-dscp>60</ip-dscp>
                <ip-ecn>3</ip-ecn>
            </ip-match>
            <tcp-source-port>183</tcp-source-port>
            <tcp-destination-port>8080</tcp-destination-port>
        </match>
    </flow>

Output to INPORT
''''''''''''''''

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf102</flow-name>
        <id>257</id>
        <cookie_mask>255</cookie_mask>
        <cookie>102</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <output-action>
                            <output-node-connector>INPORT</output-node-connector>
                            <max-length>60</max-length>
                        </output-action>
                    </action>
    7            </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>ff:ff:29:01:19:61</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:11:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <ipv4-source>17.1.2.3/8</ipv4-source>
            <ipv4-destination>172.168.5.6/16</ipv4-destination>
            <ip-match>
                <ip-protocol>6</ip-protocol>
                <ip-dscp>2</ip-dscp>
                <ip-ecn>2</ip-ecn>
            </ip-match>
            <tcp-source-port>25364</tcp-source-port>
            <tcp-destination-port>8080</tcp-destination-port>
        </match>
    </flow>

Output to Physical Port
'''''''''''''''''''''''

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf103</flow-name>
        <id>258</id>
        <cookie_mask>255</cookie_mask>
        <cookie>103</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <output-action>
                            <output-node-connector>1</output-node-connector>
                            <max-length>60</max-length>
                        </output-action>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>ff:ff:29:01:19:61</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:11:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <ipv4-source>17.1.2.3/8</ipv4-source>
            <ipv4-destination>172.168.5.6/16</ipv4-destination>
            <ip-match>
                <ip-protocol>6</ip-protocol>
                <ip-dscp>2</ip-dscp>
                <ip-ecn>2</ip-ecn>
            </ip-match>
            <tcp-source-port>25364</tcp-source-port>
            <tcp-destination-port>8080</tcp-destination-port>
        </match>
    </flow>

Output to LOCAL
'''''''''''''''

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf104</flow-name>
        <id>259</id>
        <cookie_mask>255</cookie_mask>
        <cookie>104</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <output-action>
                            <output-node-connector>LOCAL</output-node-connector>
                            <max-length>60</max-length>
                        </output-action>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34525</type>
                </ethernet-type>
            </ethernet-match>
            <ipv6-source>1234:5678:9ABC:DEF0:FDCD:A987:6543:210F/76</ipv6-source>
            <ipv6-destination>fe80:2acf:e9ff:fe21::6431/94</ipv6-destination>
            <metadata>
                <metadata>12345</metadata>
            </metadata>
            <ip-match>
                <ip-protocol>6</ip-protocol>
                <ip-dscp>60</ip-dscp>
                <ip-ecn>3</ip-ecn>
            </ip-match>
            <tcp-source-port>183</tcp-source-port>
            <tcp-destination-port>8080</tcp-destination-port>
        </match>
    </flow>

Output to NORMAL
''''''''''''''''

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf105</flow-name>
        <id>260</id>
        <cookie_mask>255</cookie_mask>
        <cookie>105</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <output-action>
                            <output-node-connector>NORMAL</output-node-connector>
                            <max-length>60</max-length>
                        </output-action>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34525</type>
                </ethernet-type>
            </ethernet-match>
            <ipv6-source>1234:5678:9ABC:DEF0:FDCD:A987:6543:210F/84</ipv6-source>
            <ipv6-destination>fe80:2acf:e9ff:fe21::6431/90</ipv6-destination>
            <metadata>
                <metadata>12345</metadata>
            </metadata>
            <ip-match>
                <ip-protocol>6</ip-protocol>
                <ip-dscp>45</ip-dscp>
                <ip-ecn>2</ip-ecn>
            </ip-match>
            <tcp-source-port>20345</tcp-source-port>
            <tcp-destination-port>80</tcp-destination-port>
        </match>
    </flow>

Output to FLOOD
'''''''''''''''

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf106</flow-name>
        <id>261</id>
        <cookie_mask>255</cookie_mask>
        <cookie>106</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <output-action>
                            <output-node-connector>FLOOD</output-node-connector>
                            <max-length>60</max-length>
                        </output-action>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34525</type>
                </ethernet-type>
            </ethernet-match>
            <ipv6-source>1234:5678:9ABC:DEF0:FDCD:A987:6543:210F/100</ipv6-source>
            <ipv6-destination>fe80:2acf:e9ff:fe21::6431/67</ipv6-destination>
            <metadata>
                <metadata>12345</metadata>
            </metadata>
            <ip-match>
                <ip-protocol>6</ip-protocol>
                <ip-dscp>45</ip-dscp>
                <ip-ecn>2</ip-ecn>
            </ip-match>
            <tcp-source-port>20345</tcp-source-port>
            <tcp-destination-port>80</tcp-destination-port>
        </match>
    </flow>

Output to ALL
'''''''''''''

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf107</flow-name>
        <id>262</id>
        <cookie_mask>255</cookie_mask>
        <cookie>107</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <output-action>
                            <output-node-connector>ALL</output-node-connector>
                            <max-length>60</max-length>
                        </output-action>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>20:14:29:01:19:61</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:11:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <ipv4-source>19.1.2.3/10</ipv4-source>
            <ipv4-destination>172.168.5.6/18</ipv4-destination>
            <ip-match>
                <ip-protocol>17</ip-protocol>
                <ip-dscp>8</ip-dscp>
                <ip-ecn>3</ip-ecn>
            </ip-match>
            <udp-source-port>25364</udp-source-port>
            <udp-destination-port>8080</udp-destination-port>
            <in-port>0</in-port>
        </match>
    </flow>

Output to CONTROLLER
''''''''''''''''''''

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf108</flow-name>
        <id>263</id>
        <cookie_mask>255</cookie_mask>
        <cookie>108</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <output-action>
                            <output-node-connector>CONTROLLER</output-node-connector>
                            <max-length>60</max-length>
                        </output-action>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>20:14:29:01:19:61</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:11:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <ipv4-source>19.1.2.3/10</ipv4-source>
            <ipv4-destination>172.168.5.6/18</ipv4-destination>
            <ip-match>
                <ip-protocol>17</ip-protocol>
                <ip-dscp>8</ip-dscp>
                <ip-ecn>3</ip-ecn>
            </ip-match>
            <udp-source-port>25364</udp-source-port>
            <udp-destination-port>8080</udp-destination-port>
            <in-port>0</in-port>
        </match>
    </flow>

Output to ANY
'''''''''''''

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
        <strict>false</strict>
        <flow-name>FooXf109</flow-name>
        <id>264</id>
        <cookie_mask>255</cookie_mask>
        <cookie>109</cookie>
        <table_id>2</table_id>
        <priority>2</priority>
        <hard-timeout>1200</hard-timeout>
        <idle-timeout>3400</idle-timeout>
        <installHw>false</installHw>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <order>0</order>
                        <output-action>
                            <output-node-connector>ANY</output-node-connector>
                            <max-length>60</max-length>
                        </output-action>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
                <ethernet-destination>
                    <address>20:14:29:01:19:61</address>
                </ethernet-destination>
                <ethernet-source>
                    <address>00:00:00:11:23:ae</address>
                </ethernet-source>
            </ethernet-match>
            <ipv4-source>19.1.2.3/10</ipv4-source>
            <ipv4-destination>172.168.5.6/18</ipv4-destination>
            <ip-match>
                <ip-protocol>17</ip-protocol>
                <ip-dscp>8</ip-dscp>
                <ip-ecn>3</ip-ecn>
            </ip-match>
            <udp-source-port>25364</udp-source-port>
            <udp-destination-port>8080</udp-destination-port>
            <in-port>0</in-port>
        </match>
    </flow>

Push VLAN
'''''''''

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow xmlns="urn:opendaylight:flow:inventory">
       <strict>false</strict>
       <instructions>
           <instruction>
               <order>0</order>
               <apply-actions>
                  <action>
                     <push-vlan-action>
                         <ethernet-type>33024</ethernet-type>
                     </push-vlan-action>
                     <order>0</order>
                  </action>
                   <action>
                       <set-field>
                           <vlan-match>
                                <vlan-id>
                                    <vlan-id>79</vlan-id>
                                    <vlan-id-present>true</vlan-id-present>
                                </vlan-id>
                           </vlan-match>
                       </set-field>
                       <order>1</order>
                   </action>
                   <action>
                       <output-action>
                           <output-node-connector>5</output-node-connector>
                       </output-action>
                       <order>2</order>
                   </action>
               </apply-actions>
           </instruction>
       </instructions>
       <table_id>0</table_id>
       <id>31</id>
       <match>
           <ethernet-match>
               <ethernet-type>
                   <type>2048</type>
               </ethernet-type>
               <ethernet-destination>
                   <address>FF:FF:29:01:19:61</address>
               </ethernet-destination>
               <ethernet-source>
                   <address>00:00:00:11:23:AE</address>
               </ethernet-source>
           </ethernet-match>
         <in-port>1</in-port>
       </match>
       <flow-name>vlan_flow</flow-name>
       <priority>2</priority>
    </flow>

Push MPLS
'''''''''

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow
        xmlns="urn:opendaylight:flow:inventory">
        <flow-name>push-mpls-action</flow-name>
        <instructions>
            <instruction>
                <order>3</order>
                <apply-actions>
                    <action>
                        <push-mpls-action>
                            <ethernet-type>34887</ethernet-type>
                        </push-mpls-action>
                        <order>0</order>
                    </action>
                    <action>
                        <set-field>
                            <protocol-match-fields>
                                <mpls-label>27</mpls-label>
                            </protocol-match-fields>
                        </set-field>
                        <order>1</order>
                    </action>
                    <action>
                        <output-action>
                            <output-node-connector>2</output-node-connector>
                        </output-action>
                        <order>2</order>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <strict>false</strict>
        <id>100</id>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>2048</type>
                </ethernet-type>
            </ethernet-match>
            <in-port>1</in-port>
            <ipv4-destination>10.0.0.4/32</ipv4-destination>
        </match>
        <idle-timeout>0</idle-timeout>
        <cookie_mask>255</cookie_mask>
        <cookie>401</cookie>
        <priority>8</priority>
        <hard-timeout>0</hard-timeout>
        <installHw>false</installHw>
        <table_id>0</table_id>
    </flow>

Swap MPLS
'''''''''

-  Note that ethernet-type MUST be 34887

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow
        xmlns="urn:opendaylight:flow:inventory">
        <flow-name>push-mpls-action</flow-name>
        <instructions>
            <instruction>
                <order>2</order>
                <apply-actions>
                    <action>
                        <set-field>
                            <protocol-match-fields>
                                <mpls-label>37</mpls-label>
                            </protocol-match-fields>
                        </set-field>
                        <order>1</order>
                    </action>
                    <action>
                        <output-action>
                            <output-node-connector>2</output-node-connector>
                        </output-action>
                        <order>2</order>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <strict>false</strict>
        <id>101</id>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34887</type>
                </ethernet-type>
            </ethernet-match>
            <in-port>1</in-port>
            <protocol-match-fields>
                <mpls-label>27</mpls-label>
            </protocol-match-fields>
        </match>
        <idle-timeout>0</idle-timeout>
        <cookie_mask>255</cookie_mask>
        <cookie>401</cookie>
        <priority>8</priority>
        <hard-timeout>0</hard-timeout>
        <installHw>false</installHw>
        <table_id>0</table_id>
    </flow>

Pop MPLS
''''''''

-  Note that ethernet-type MUST be 34887

-  Issue with OVS 2.1 `OVS
   fix <http://git.openvswitch.org/cgi-bin/gitweb.cgi?p=openvswitch;a=commitdiff;h=b3f2fc93e3f357f8d05a92f53ec253339a40887f>`__

.. code:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <flow
        xmlns="urn:opendaylight:flow:inventory">
        <flow-name>FooXf10</flow-name>
        <instructions>
            <instruction>
                <order>0</order>
                <apply-actions>
                    <action>
                        <pop-mpls-action>
                            <ethernet-type>2048</ethernet-type>
                        </pop-mpls-action>
                        <order>1</order>
                    </action>
                    <action>
                        <output-action>
                            <output-node-connector>2</output-node-connector>
                            <max-length>60</max-length>
                        </output-action>
                        <order>2</order>
                    </action>
                </apply-actions>
            </instruction>
        </instructions>
        <id>11</id>
        <strict>false</strict>
        <match>
            <ethernet-match>
                <ethernet-type>
                    <type>34887</type>
                </ethernet-type>
            </ethernet-match>
            <in-port>1</in-port>
            <protocol-match-fields>
                <mpls-label>37</mpls-label>
            </protocol-match-fields>
        </match>
        <idle-timeout>0</idle-timeout>
        <cookie>889</cookie>
        <cookie_mask>255</cookie_mask>
        <installHw>false</installHw>
        <hard-timeout>0</hard-timeout>
        <priority>10</priority>
        <table_id>0</table_id>
    </flow>

Opendaylight OpenFlow Plugin: Troubleshooting
---------------------------------------------

empty section

OpFlex agent-ovs User Guide
===========================

Introduction
------------

agent-ovs is a policy agent that works with OVS to enforce a group-based
policy networking model with locally attached virtual machines or
containers. The policy agent is designed to work well with orchestration
tools like OpenStack.

Agent Configuration
-------------------

The agent configuration is handled using its config file which is by
default found at "/etc/opflex-agent-ovs/opflex-agent-ovs.conf"

Here is an example configuration file that documents the available
options:

::

    {
        // Logging configuration
        // "log": {
        //    "level": "info"
        // },

        // Configuration related to the OpFlex protocol
        "opflex": {
            // The policy domain for this agent.
            "domain": "openstack",

            // The unique name in the policy domain for this agent.
            "name": "example-agent",

            // a list of peers to connect to, by hostname and port.  One
            // peer, or an anycast pseudo-peer, is sufficient to bootstrap
            // the connection without needing an exhaustive list of all
            // peers.
            "peers": [
                // EXAMPLE:
                {"hostname": "10.0.0.30", "port": 8009}
            ],

            "ssl": {
                // SSL mode.  Possible values:
                // disabled: communicate without encryption
                // encrypted: encrypt but do not verify peers
                // secure: encrypt and verify peer certificates
                "mode": "disabled",

                // The path to a directory containing trusted certificate
                // authority public certificates, or a file containing a
                // specific CA certificate.
                "ca-store": "/etc/ssl/certs/"
            },

            "inspector": {
                // Enable the MODB inspector service, which allows
                // inspecting the state of the managed object database.
            // Default: enabled
                "enabled": true,

                // Listen on the specified socket for the inspector
            // Default /var/run/opflex-agent-ovs-inspect.sock
                "socket-name": "/var/run/opflex-agent-ovs-inspect.sock"
            }
        },

        // Endpoint sources provide metadata about local endpoints
        "endpoint-sources": {
            // Filesystem path to monitor for endpoint information
            "filesystem": ["/var/lib/opflex-agent-ovs/endpoints"]
        },

        // Renderers enforce policy obtained via OpFlex.
        "renderers": {
            // Stitched-mode renderer for interoperating with a
            // hardware fabric such as ACI
            // EXAMPLE:
            "stitched-mode": {
                "ovs-bridge-name": "br0",

                // Set encapsulation type.  Must set either vxlan or vlan.
                "encap": {
                    // Encapsulate traffic with VXLAN.
                    "vxlan" : {
                        // The name of the tunnel interface in OVS
                        "encap-iface": "br0_vxlan0",

                        // The name of the interface whose IP should be used
                        // as the source IP in encapsulated traffic.
                        "uplink-iface": "eth0.4093",

                        // The vlan tag, if any, used on the uplink interface.
                        // Set to zero or omit if the uplink is untagged.
                        "uplink-vlan": 4093,

                        // The IP address used for the destination IP in
                        // the encapsulated traffic.  This should be an
                        // anycast IP address understood by the upstream
                        // stiched-mode fabric.
                        "remote-ip": "10.0.0.32",

                        // UDP port number of the encapsulated traffic.
                        "remote-port": 8472
                    }

                    // Encapsulate traffic with a locally-significant VLAN
                    // tag
                    // EXAMPLE:
                    // "vlan" : {
                    //     // The name of the uplink interface in OVS
                    //     "encap-iface": "team0"
                    // }
                },

                // Configure forwarding policy
                "forwarding": {
                    // Configure the virtual distributed router
                    "virtual-router": {
                        // Enable virtual distributed router.  Set to true
                        // to enable or false to disable.  Default true.
                        "enabled": true,

                        // Override MAC address for virtual router.
                        // Default is "00:22:bd:f8:19:ff"
                        "mac": "00:22:bd:f8:19:ff",

                        // Configure IPv6-related settings for the virtual
                        // router
                        "ipv6" : {
                            // Send router advertisement messages in
                            // response to router solicitation requests as
                            // well as unsolicited advertisements.  This
                            // is not required in stitched mode since the
                            // hardware router will send them.
                            "router-advertisement": true
                        }
                    },

                    // Configure virtual distributed DHCP server
                    "virtual-dhcp": {
                        // Enable virtual distributed DHCP server.  Set to
                        // true to enable or false to disable.  Default
                        // true.
                        "enabled": true,

                        // Override MAC address for virtual dhcp server.
                        // Default is "00:22:bd:f8:19:ff"
                        "mac": "00:22:bd:f8:19:ff"
                    },

                    "endpoint-advertisements": {
                        // Enable generation of periodic ARP/NDP
                        // advertisements for endpoints.  Default true.
                        "enabled": "true"
                    }
                },

                // Location to store cached IDs for managing flow state
                "flowid-cache-dir": "/var/lib/opflex-agent-ovs/ids"
            }
        }
    }

Endpoint Registration
---------------------

The agent learns about endpoints using endpoint metadata files located
by default in "/var/lib/opflex-agent-ovs/endpoints".

These are JSON-format files such as the (unusually complex) example
below:

::

    {
        "uuid": "83f18f0b-80f7-46e2-b06c-4d9487b0c754",
        "policy-space-name": "test",
        "endpoint-group-name": "group1",
        "interface-name": "veth0",
        "ip": [
            "10.0.0.1", "fd8f:69d8:c12c:ca62::1"
        ],
        "dhcp4": {
            "ip": "10.200.44.2",
            "prefix-len": 24,
            "routers": ["10.200.44.1"],
            "dns-servers": ["8.8.8.8", "8.8.4.4"],
            "domain": "example.com",
            "static-routes": [
                {
                    "dest": "169.254.169.0",
                    "dest-prefix": 24,
                    "next-hop": "10.0.0.1"
                }
            ]
        },
        "dhcp6": {
            "dns-servers": ["2001:4860:4860::8888", "2001:4860:4860::8844"],
            "search-list": ["test1.example.com", "example.com"]
        },
        "ip-address-mapping": [
            {
               "uuid": "91c5b217-d244-432c-922d-533c6c036ab4",
               "floating-ip": "5.5.5.1",
               "mapped-ip": "10.0.0.1",
               "policy-space-name": "common",
               "endpoint-group-name": "nat-epg"
            },
            {
               "uuid": "22bfdc01-a390-4b6f-9b10-624d4ccb957b",
               "floating-ip": "fdf1:9f86:d1af:6cc9::1",
               "mapped-ip": "fd8f:69d8:c12c:ca62::1",
               "policy-space-name": "common",
               "endpoint-group-name": "nat-epg"
            }
        ],
        "mac": "00:00:00:00:00:01",
        "promiscuous-mode": false
    }

The possible parameters for these files are:

**uuid**
    A globally unique ID for the endpoint

**endpoint-group-name**
    The name of the endpoint group for the endpoint

**policy-space-name**
    The name of the policy space for the endpoint group.

**interface-name**
    The name of the OVS interface to which the endpoint is attached

**ip**
    A list of strings contains either IPv4 or IPv6 addresses that the
    endpoint is allowed to use

**mac**
    The MAC address for the endpoint’s interface.

**promiscuous-mode**
    Allow traffic from this VM to bypass default port security

**dhcp4**
    A distributed DHCPv4 configuration block (see below)

**dhcp6**
    A distributed DHCPv6 configuration block (see below)

**ip-address-mapping**
    A list of IP address mapping configuration blocks (see below)

DHCPv4 configuration blocks can contain the following parameters:

**ip**
    the IP address to return with DHCP. Must be one of the configured
    IPv4 addresses.

**prefix**
    the subnet prefix length

**routers**
    a list of default gateways for the endpoint

**dns**
    a list of DNS server addresses

**domain**
    The domain name parameter to send in the DHCP reply

**static-routes**
    A list of static route configuration blocks, which contains a
    "dest", "dest-prefix", and "next-hop" parameters to send as static
    routes to the end host

DHCPv6 configuration blocks can contain the following parameters:

**dns**
    A list of DNS servers for the endpoint

**search-patch**
    The DNS search path for the endpoint

IP address mapping configuration blocks can contain the following
parameters:

**uuid**
    a globally unique ID for the virtual endpoint created by the
    mapping.

**floating-ip**
    Map using DNAT to this floating IPv4 or IPv6 address

**mapped-ip**
    the source IPv4 or IPv6 address; must be one of the IPs assigned to
    the endpoint.

**endpoint-group-name**
    The name of the endpoint group for the NATed IP

**policy-space-name**
    The name of the policy space for the NATed IP

Inspector
---------

The Opflex inspector is a useful command-line tool that will allow you
to inspect the state of the managed object database for the agent for
debugging and diagnosis purposes.

The command is called "gbp\_inspect" and takes the following arguments:

::

    # gbp_inspect -h
    Usage: ./gbp_inspect [options]
    Allowed options:
      -h [ --help ]                         Print this help message
      --log arg                             Log to the specified file (default
                                            standard out)
      --level arg (=warning)                Use the specified log level (default
                                            info)
      --syslog                              Log to syslog instead of file or
                                            standard out
      --socket arg (=/usr/local/var/run/opflex-agent-ovs-inspect.sock)
                                            Connect to the specified UNIX domain
                                            socket (default /usr/local/var/run/opfl
                                            ex-agent-ovs-inspect.sock)
      -q [ --query ] arg                    Query for a specific object with
                                            subjectname,uri or all objects of a
                                            specific type with subjectname
      -r [ --recursive ]                    Retrieve the whole subtree for each
                                            returned object
      -f [ --follow-refs ]                  Follow references in returned objects
      --load arg                            Load managed objects from the specified
                                            file into the MODB view
      -o [ --output ] arg                   Output the results to the specified
                                            file (default standard out)
      -t [ --type ] arg (=tree)             Specify the output format: tree, list,
                                            or dump (default tree)
      -p [ --props ]                        Include object properties in output

Here are some examples of the ways to use this tool.

You can get information about the running system using one or more
queries, which consist of an object model class name and optionally the
URI of a specific object. The simplest query is to get a single object,
nonrecursively:

::

    # gbp_inspect -q DmtreeRoot
    --* DmtreeRoot,/
    # gbp_inspect -q GbpEpGroup
    --* GbpEpGroup,/PolicyUniverse/PolicySpace/common/GbpEpGroup/nat-epg/
    --* GbpEpGroup,/PolicyUniverse/PolicySpace/test/GbpEpGroup/group1/
    # gbp_inspect -q GbpEpGroup,/PolicyUniverse/PolicySpace/common/GbpEpGroup/nat-epg/
    --* GbpEpGroup,/PolicyUniverse/PolicySpace/common/GbpEpGroup/nat-epg/

You can also display all the properties for each object:

::

    # gbp_inspect -p -q GbpeL24Classifier
    --* GbpeL24Classifier,/PolicyUniverse/PolicySpace/test/GbpeL24Classifier/classifier4/
         {
           connectionTracking : 1 (reflexive)
           dFromPort          : 80
           dToPort            : 80
           etherT             : 2048 (ipv4)
           name               : classifier4
           prot               : 6
         }
    --* GbpeL24Classifier,/PolicyUniverse/PolicySpace/test/GbpeL24Classifier/classifier3/
         {
           etherT : 34525 (ipv6)
           name   : classifier3
           order  : 100
           prot   : 58
         }
    --* GbpeL24Classifier,/PolicyUniverse/PolicySpace/test/GbpeL24Classifier/classifier2/
         {
           etherT : 2048 (ipv4)
           name   : classifier2
           order  : 101
           prot   : 1
         }

You can also request to get the all the children of an object you query
for:

::

    # gbp_inspect -r -q GbpEpGroup,/PolicyUniverse/PolicySpace/common/GbpEpGroup/nat-epg/
    --* GbpEpGroup,/PolicyUniverse/PolicySpace/common/GbpEpGroup/nat-epg/
      |-* GbpeInstContext,/PolicyUniverse/PolicySpace/common/GbpEpGroup/nat-epg/GbpeInstContext/
      `-* GbpEpGroupToNetworkRSrc,/PolicyUniverse/PolicySpace/common/GbpEpGroup/nat-epg/GbpEpGroupToNetworkRSrc/

You can also follow references found in any object downloads:

::

    # gbp_inspect -fr -q GbpEpGroup,/PolicyUniverse/PolicySpace/common/GbpEpGroup/nat-epg/
    --* GbpEpGroup,/PolicyUniverse/PolicySpace/common/GbpEpGroup/nat-epg/
      |-* GbpeInstContext,/PolicyUniverse/PolicySpace/common/GbpEpGroup/nat-epg/GbpeInstContext/
      `-* GbpEpGroupToNetworkRSrc,/PolicyUniverse/PolicySpace/common/GbpEpGroup/nat-epg/GbpEpGroupToNetworkRSrc/
    --* GbpFloodDomain,/PolicyUniverse/PolicySpace/common/GbpFloodDomain/fd_ext/
      `-* GbpFloodDomainToNetworkRSrc,/PolicyUniverse/PolicySpace/common/GbpFloodDomain/fd_ext/GbpFloodDomainToNetworkRSrc/
    --* GbpBridgeDomain,/PolicyUniverse/PolicySpace/common/GbpBridgeDomain/bd_ext/
      `-* GbpBridgeDomainToNetworkRSrc,/PolicyUniverse/PolicySpace/common/GbpBridgeDomain/bd_ext/GbpBridgeDomainToNetworkRSrc/
    --* GbpRoutingDomain,/PolicyUniverse/PolicySpace/common/GbpRoutingDomain/rd_ext/
      |-* GbpRoutingDomainToIntSubnetsRSrc,/PolicyUniverse/PolicySpace/common/GbpRoutingDomain/rd_ext/GbpRoutingDomainToIntSubnetsRSrc/122/%2fPolicyUniverse%2fPolicySpace%2fcommon%2fGbpSubnets%2fsubnets_ext%2f/
      `-* GbpForwardingBehavioralGroupToSubnetsRSrc,/PolicyUniverse/PolicySpace/common/GbpRoutingDomain/rd_ext/GbpForwardingBehavioralGroupToSubnetsRSrc/
    --* GbpSubnets,/PolicyUniverse/PolicySpace/common/GbpSubnets/subnets_ext/
      |-* GbpSubnet,/PolicyUniverse/PolicySpace/common/GbpSubnets/subnets_ext/GbpSubnet/subnet_ext4/
      `-* GbpSubnet,/PolicyUniverse/PolicySpace/common/GbpSubnets/subnets_ext/GbpSubnet/subnet_ext6/

PCEP User Guide
===============

Overview
--------

The OpenDaylight Karaf distribution comes preconfigured with baseline
PCEP configuration.

-  **32-pcep.xml** (basic PCEP configuration, including session
   parameters)

-  **39-pcep-provider.xml** (configuring for PCEP provider)

Configuring PCEP
----------------

The default shipped configuration will start a PCE server on
0.0.0.0:4189. You can change this behavior in **39-pcep-provider.xml**:

.. code:: xml

    <module>
     <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:pcep:topology:provider">prefix:pcep-topology-provider</type>
     <name>pcep-topology</name>
     <listen-address>192.168.122.55</listen-address>
     <listen-port>4189</listen-port>
    ...
    </module>

-  **listen-address** - adress on which PCE will be started and listen

-  **listen-port** - port on which the address will be started and
   listen

PCEP default configuration is set to conform stateful PCEP extension:

`draft-ietf-pce-stateful-pce <http://tools.ietf.org/html/draft-ietf-pce-stateful-pce>`__
- in versions 02 and 07

PCEP Segment Routing
~~~~~~~~~~~~~~~~~~~~

Conforms
`draft-eitf-pce-segment-routing <http://tools.ietf.org/html/draft-ietf-pce-segment-routing-01>`__
- PCEP extension for Segment Routing

The default configuration file is located in etc/opendaylight/karaf.

-  **33-pcep-segment-routing.xml** - You don’t need to edit this file.

PacketCable User Guide
======================

Overview
--------

These components introduce a DOCSIS QoS Gates management using the PCMM
protocol. The driver component is responsible for the PCMM/COPS/PDP
functionality required to service requests from PacketCable Provider and
FlowManager. Requests are transposed into PCMM Gate Control messages and
transmitted via COPS to the CMTS. This plugin adheres to the
PCMM/COPS/PDP functionality defined in the CableLabs specification.
PacketCable solution is an MDSAL compliant component.

PacketCable Components
----------------------

PacketCable is comprised of two OpenDaylight bundles:

+--------------------------------------+--------------------------------------+
| Bundle                               | Description                          |
+======================================+======================================+
| odl-packetcable-policy-server        | Plugin that provides PCMM model      |
|                                      | implementation based on CMTS         |
|                                      | structure and COPS protocol.         |
+--------------------------------------+--------------------------------------+
| odl-packetcable-policy-model         | The Model provided provides a direct |
|                                      | mapping to the underlying QoS Gates  |
|                                      | of CMTS.                             |
+--------------------------------------+--------------------------------------+

See the PacketCable `YANG
Models <https://git.opendaylight.org/gerrit/gitweb?p=packetcable.git;a=tree;f=packetcable-policy-model/src/main/yang>`__.

Installing PacketCable
----------------------

To install PacketCable, run the following ``feature:install`` command
from the Karaf CLI

::

    feature:install odl-packetcable-policy-server-all odl-restconf odl-mdsal-apidocs

Explore and exercise the PacketCable REST API
---------------------------------------------

To see the PacketCable APIs, browse to this URL:
http://localhost:8181/apidoc/explorer/index.html

Replace localhost with the IP address or hostname where OpenDaylight is
running if you are not running OpenDaylight locally on your machine.

    **Note**

    Prior to setting any PCMM gates, a CCAP must first be added.

Postman
-------

`Install the Chrome
extension <https://chrome.google.com/webstore/detail/postman-rest-client/fdmmgilgnpjigdojojpjoooidkmcomcm?hl=en>`__

`Download and import sample packetcable
collection <https://git.opendaylight.org/gerrit/gitweb?p=packetcable.git;a=tree;f=packetcable-policy-server/doc/restconf-samples>`__

.. figure:: ./images/Screenshot5.png
   :alt: Postman Operations

   Postman Operations

Service Function Chaining
=========================

OpenDaylight Service Function Chaining (SFC) Overiew
----------------------------------------------------

OpenDaylight Service Function Chaining (SFC) provides the ability to
define an ordered list of a network services (e.g. firewalls, load
balancers). These service are then "stitched" together in the network to
create a service chain. This project provides the infrastructure
(chaining logic, APIs) needed for ODL to provision a service chain in
the network and an end-user application for defining such chains.

-  ACE - Access Control Entry

-  ACL - Access Control List

-  SCF - Service Classifier Function

-  SF - Service Function

-  SFC - Service Function Chain

-  SFF - Service Function Forwarder

-  SFG - Service Function Group

-  SFP - Service Function Path

-  RSP - Rendered Service Path

-  NSH - Network Service Header

SFC User Interface
------------------

Overview
~~~~~~~~

SFC User Interface (SFC-UI) is based on Dlux project. It provides an
easy way to create, read, update and delete configuration stored in
Datastore. Moreover, it shows the status of all SFC features (e.g
installed, uninstalled) and Karaf log messages as well.

SFC-UI Architecture
~~~~~~~~~~~~~~~~~~~

SFC-UI operates purely by using RESTCONF.

.. figure:: ./images/sfc/sfc-ui-architecture.png
   :alt: SFC-UI integration into ODL

   SFC-UI integration into ODL

Configuring SFC-UI
~~~~~~~~~~~~~~~~~~

1. Run ODL distribution (run karaf)

2. In karaf console execute: ``feature:install odl-sfc-ui``

3. Visit SFC-UI on: ``http://<odl_ip_address>:8181/sfc/index.html``

SFC Southbound REST Plugin
--------------------------

Overview
~~~~~~~~

The Southbound REST Plugin is used to send configuration from DataStore
down to network devices supporting a REST API (i.e. they have a
configured REST URI). It supports POST/PUT/DELETE operations, which are
triggered accordingly by changes in the SFC data stores.

-  Access Control List (ACL)

-  Service Classifier Function (SCF)

-  Service Function (SF)

-  Service Function Group (SFG)

-  Service Function Schedule Type (SFST)

-  Service Function Forwader (SFF)

-  Rendered Service Path (RSP)

Southbound REST Plugin Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the user perspective, the REST plugin is another SFC Southbound
plugin used to communicate with network devices.

.. figure:: ./images/sfc/sb-rest-architecture-user.png
   :alt: Soutbound REST Plugin integration into ODL

   Soutbound REST Plugin integration into ODL

Configuring Southbound REST Plugin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Run ODL distribution (run karaf)

2. In karaf console execute: ``feature:install odl-sfc-sb-rest``

3. Configure REST URIs for SF/SFF through SFC User Interface or RESTCONF
   (required configuration steps can be found in the tutorial stated
   bellow)

Tutorial
~~~~~~~~

Comprehensive tutorial on how to use the Southbound REST Plugin and how
to control network devices with it can be found on:
https://wiki.opendaylight.org/view/Service_Function_Chaining:Main#SFC_101

SFC-OVS integration
-------------------

Overview
~~~~~~~~

SFC-OVS provides integration of SFC with Open vSwitch (OVS) devices.
Integration is realized through mapping of SFC objects (like SF, SFF,
Classifier, etc.) to OVS objects (like Bridge,
TerminationPoint=Port/Interface). The mapping takes care of automatic
instantiation (setup) of corresponding object whenever its counterpart
is created. For example, when a new SFF is created, the SFC-OVS plugin
will create a new OVS bridge and when a new OVS Bridge is created, the
SFC-OVS plugin will create a new SFF.

The feature is intended for SFC users willing to use Open vSwitch as
underlying network infrastructure for deploying RSPs (Rendered Service
Paths).

SFC-OVS Architecture
~~~~~~~~~~~~~~~~~~~~

SFC-OVS uses the OVSDB MD-SAL Southbound API for getting/writing
information from/to OVS devices. From the user perspective SFC-OVS acts
as a layer between SFC DataStore and OVSDB.

.. figure:: ./images/sfc/sfc-ovs-architecture-user.png
   :alt: SFC-OVS integration into ODL

   SFC-OVS integration into ODL

Configuring SFC-OVS
~~~~~~~~~~~~~~~~~~~

1. Run ODL distribution (run karaf)

2. In karaf console execute: ``feature:install odl-sfc-ovs``

3. Configure Open vSwitch to use ODL as a manager, using following
   command: ``ovs-vsctl set-manager tcp:<odl_ip_address>:6640``

Tutorials
~~~~~~~~~

Verifying mapping from OVS to SFF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Overview
''''''''

This tutorial shows the usual workflow when OVS configuration is
transformed to corresponding SFC objects (in this case SFF).

Prerequisities
''''''''''''''

-  Open vSwitch installed (ovs-vsctl command available in shell)

-  SFC-OVS feature configured as stated above

Instructions
''''''''''''

1. ``ovs-vsctl set-manager tcp:<odl_ip_address>:6640``

2. ``ovs-vsctl add-br br1``

3. ``ovs-vsctl add-port br1 testPort``

Verification
''''''''''''

a. visit SFC User Interface:
   ``http://<odl_ip_address>:8181/sfc/index.html#/sfc/serviceforwarder``

b. use pure RESTCONF and send GET request to URL:
   ``http://<odl_ip_address>:8181/restconf/config/service-function-forwarder:service-function-forwarders``

There should be SFF, which name will be ending with *br1* and the SFF
should containt two DataPlane locators: *br1* and *testPort*.

Verifying mapping from SFF to OVS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Overview
''''''''

This tutorial shows the usual workflow during creation of OVS Bridge
with use of SFC APIs.

Prerequisities
''''''''''''''

-  Open vSwitch installed (ovs-vsctl command available in shell)

-  SFC-OVS feature configured as stated above

Instructions
''''''''''''

1. In shell execute: ``ovs-vsctl set-manager tcp:<odl_ip_address>:6640``

2. Send POST request to URL:
   ``http://<odl_ip_address>:8181/restconf/operations/service-function-forwarder-ovs:create-ovs-bridge``
   Use Basic auth with credentials: "admin", "admin" and set
   ``Content-Type: application/json``. The content of POST request
   should be following:

::

    {
        "input":
        {
            "name": "br-test",
            "ovs-node": {
                "ip": "<Open_vSwitch_ip_address>"
            }
        }
    }

Open\_vSwitch\_ip\_address is IP address of machine, where Open vSwitch
is installed.

Verification
''''''''''''

In shell execute: ``ovs-vsctl show``. There should be Bridge with name
*br-test* and one port/interface called *br-test*.

Also, corresponding SFF for this OVS Bridge should be configured, which
can be verified through SFC User Interface or RESTCONF as stated in
previous tutorial.

SFC Classifier User Guide
-------------------------

Overview
~~~~~~~~

Description of classifier can be found in:
https://datatracker.ietf.org/doc/draft-ietf-sfc-architecture/

There are two types of classifier:

1. OpenFlow Classifier

2. Iptables Classifier

OpenFlow Classifier
~~~~~~~~~~~~~~~~~~~

OpenFlow Classifier implements the classification criteria based on
OpenFlow rules deployed into an OpenFlow switch. An Open vSwitch will
take the role of a classifier and performs various encapsulations such
NSH, VLAN, MPLS, etc. In the existing implementation, classifier can
support NSH encapsulation. Matching information is based on ACL for MAC
addresses, ports, protocol, IPv4 and IPv6. Supported protocols are TCP,
UDP and SCTP. Actions information in the OF rules, shall be forwarding
of the encapsulated packets with specific information related to the
RSP.

Classifier Architecture
^^^^^^^^^^^^^^^^^^^^^^^

The OVSDB Southbound interface is used to create an instance of a bridge
in a specific location (via IP address). This bridge contains the
OpenFlow rules that perform the classification of the packets and react
accordingly. The OpenFlow Southbound interface is used to translate the
ACL information into OF rules within the Open vSwitch.

    **Note**

    in order to create the instance of the bridge that takes the role of
    a classifier, an "empty" SFF must be created.

Configuring Classifier
^^^^^^^^^^^^^^^^^^^^^^

1. An empty SFF must be created in order to host the ACL that contains
   the classification information.

2. SFF data plane locator must be configured

3. Classifier interface must be mannually added to SFF bridge.

Administering or Managing Classifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Classification information is based on MAC addresses, protocol, ports
and IP. ACL gathers this information and is assigned to an RSP which
turns to be a specific path for a Service Chain.

Iptables Classifier
~~~~~~~~~~~~~~~~~~~

Classifier manages everything from starting the packet listener to
creation (and removal) of appropriate ip(6)tables rules and marking
received packets accordingly. Its functionality is **available only on
Linux** as it leverdges **NetfilterQueue**, which provides access to
packets matched by an **iptables** rule. Classifier requires **root
privileges** to be able to operate.

So far it is capable of processing ACL for MAC addresses, ports, IPv4
and IPv6. Supported protocols are TCP and UDP.

Classifier Architecture
^^^^^^^^^^^^^^^^^^^^^^^

Python code located in the project repository
sfc-py/common/classifier.py.

    **Note**

    classifier assumes that Rendered Service Path (RSP) **already
    exists** in ODL when an ACL referencing it is obtained

1. sfc\_agent receives an ACL and passes it for processing to the
   classifier

2. the RSP (its SFF locator) referenced by ACL is requested from ODL

3. if the RSP exists in the ODL then ACL based iptables rules for it are
   applied

After this process is over, every packet successfully matched to an
iptables rule (i.e. successfully classified) will be NSH encapsulated
and forwarded to a related SFF, which knows how to traverse the RSP.

Rules are created using appropriate iptables command. If the Access
Control Entry (ACE) rule is MAC address related both iptables and
ip6tabeles rules re issued. If ACE rule is IPv4 address related, only
iptables rules are issued, same for IPv6.

    **Note**

    iptables **raw** table contains all created rules

Configuring Classifier
^^^^^^^^^^^^^^^^^^^^^^

| Classfier does’t need any configuration.
| Its only requirement is that the **second (2) Netfilter Queue** is not
  used by any other process and is **avalilable for the classifier**.

Administering or Managing Classifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Classfier runs alongside sfc\_agent, therefore the commad for starting
it locally is:

::

    sudo python3.4 sfc-py/sfc_agent.py --rest --odl-ip-port localhost:8181 --auto-sff-name --nfq-class

SFC OpenFlow Layer 2 Renderer User Guide
----------------------------------------

Overview
~~~~~~~~

The Service Function Chaining (SFC) OpenFlow Layer 2 Renderer (SFCOFL2)
implements Service Chaining on OpenFlow switches. It listens for the
creation of a Rendered Service Path (RSP), and once received it programs
Service Function Forwarders (SFF) that are hosted on OpenFlow capable
switches to steer packets through the service chain.

Common acronyms used in the following sections:

-  SF - Service Function

-  SFF - Service Function Forwarder

-  SFC - Service Function Chain

-  SFP - Service Function Path

-  RSP - Rendered Service Path

SFC OpenFlow Renderer Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SFCOFL2 is invoked after a RSP is created using an MD-SAL listener
called ``SfcL2RspDataListener``. Upon SFCOFL2 initialization, the
``SfcL2RspDataListener`` registers itself to listen for RSP changes.
When invoked, the ``SfcL2RspDataListener`` processes the RSP and calls
the ``SfcL2FlowProgrammerOFImpl`` to create the necessary flows in the
Service Function Forwarders configured in the RSP. Refer to the
following diagram for more details.

.. figure:: ./images/sfc/sfcofl2_architecture.jpg
   :alt: SFC OpenFlow Renderer High Level Architecture

   SFC OpenFlow Renderer High Level Architecture

SFC OpenFlow Switch Flow pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SFC OpenFlow Renderer uses the following tables for its Flow
pipeline:

-  Table 0, Transport Ingress

-  Table 1, Path Mapper

-  Table 2, Next Hop

-  Table 10, Transport Egress

The OpenFlow Table Pipeline is intended to be generic to work for all of
the different encapsulations supported by SFC.

All of the tables are explained in detail in the following section.

The SFFs (SFF1 and SFF2), SFs (SF1), and topology used for the flow
tables in the following sections are as described in the following
diagram.

.. figure:: ./images/sfc/sfcofl2_architecture_nwtopo.jpg
   :alt: SFC OpenFlow Renderer Typical Network Topology

   SFC OpenFlow Renderer Typical Network Topology

Transport Ingress Table detailed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Transport Ingress table has an entry per expected tunnel transport
type to be received in a particular SFF, as established in the SFC
configuration.

Here is an example on SFF1, assuming VLAN is used for the SFF-SF, and
the RSP tunnel is MPLS:

+--------------------------+--------------------------+--------------------------+
| Priority                 | Match                    | Action                   |
+==========================+==========================+==========================+
| 256                      | EtherType==0x8847 (MPLS  | Goto Table 1             |
|                          | unicast)                 |                          |
+--------------------------+--------------------------+--------------------------+
| 256                      | EtherType==0x8100 (VLAN) | Goto Table 1             |
+--------------------------+--------------------------+--------------------------+
| 5                        | Match Any                | Drop                     |
+--------------------------+--------------------------+--------------------------+

Table: Table Transport Ingress

Path Mapper Table detailed
^^^^^^^^^^^^^^^^^^^^^^^^^^

The Path Mapper table has an entry per expected tunnel transport info to
be received in a particular SFF, as established in the SFC
configuration. The tunnel transport info is used to determine the RSP
Path ID, and is stored in the OpenFlow Metadata.

Since most SF nodes wont support tunneling, the IP header DSCP field is
used to store the RSP Path Id. The RSP Path Id is written to the DSCP
field in the Transport Egress table for those packets sent to an SF.

Here is an example on SFF1, assuming the following details:

-  VLAN ID 1000 is used for the SFF-SF

-  The RSP Path 1 tunnel uses MPLS label 100 for ingress and 101 for
   egress

-  The RSP Path 2 (symmetric downlink path) uses MPLS label 101 for
   ingress and 100 for egress

+--------------------------+--------------------------+--------------------------+
| Priority                 | Match                    | Action                   |
+==========================+==========================+==========================+
| 256                      | MPLS Label==100          | RSP Path=1, Pop MPLS,    |
|                          |                          | Goto Table 2             |
+--------------------------+--------------------------+--------------------------+
| 256                      | MPLS Label==101          | RSP Path=2, Pop MPLS,    |
|                          |                          | Goto Table 2             |
+--------------------------+--------------------------+--------------------------+
| 256                      | VLAN ID==1000, IP        | RSP Path=1, Pop VLAN,    |
|                          | DSCP==1                  | Goto Table 2             |
+--------------------------+--------------------------+--------------------------+
| 256                      | VLAN ID==1000, IP        | RSP Path=2, Pop VLAN,    |
|                          | DSCP==2                  | Goto Table 2             |
+--------------------------+--------------------------+--------------------------+
| 5                        | Match Any                | Drop                     |
+--------------------------+--------------------------+--------------------------+

Table: Table Path Mapper

Next Hop Table detailed
^^^^^^^^^^^^^^^^^^^^^^^

The Next Hop table uses the RSP Path Id and source MAC address to
determine the destination MAC address.

Here is an example on SFF1, assuming SFF1 is connected to SFF2 and RSP
Path 1 ingress packets come from external to SFC, for which we don’t
have the source MAC address (MacSrc).

+--------------------------+--------------------------+--------------------------+
| Priority                 | Match                    | Action                   |
+==========================+==========================+==========================+
| 256                      | RSP Path==1, MacSrc==SF1 | MacDst=SFF2, Goto Table  |
|                          |                          | 10                       |
+--------------------------+--------------------------+--------------------------+
| 256                      | RSP Path==2, MacSrc==SF1 | Goto Table 10            |
+--------------------------+--------------------------+--------------------------+
| 256                      | RSP Path==2,             | MacDst=SF1, Goto Table   |
|                          | MacSrc==SFF2             | 10                       |
+--------------------------+--------------------------+--------------------------+
| 246                      | RSP Path==1              | MacDst=SF1, Goto Table   |
|                          |                          | 10                       |
+--------------------------+--------------------------+--------------------------+
| 5                        | Match Any                | Drop                     |
+--------------------------+--------------------------+--------------------------+

Table: Table Next Hop

Transport Egress Table detailed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Transport Egress table prepares egress tunnel information and sends
the packets out.

Here is an example on SFF1, assuming VLAN is used for the SFF-SF, and
the RSP tunnel is MPLS:

+--------------------------+--------------------------+--------------------------+
| Priority                 | Match                    | Action                   |
+==========================+==========================+==========================+
| 256                      | RSP Path==1, MacDst==SF1 | Push VLAN ID 1000,       |
|                          |                          | Port=SF1                 |
+--------------------------+--------------------------+--------------------------+
| 256                      | RSP Path==1,             | Push MPLS Label 101,     |
|                          | MacDst==SFF2             | Port=SFF2                |
+--------------------------+--------------------------+--------------------------+
| 256                      | RSP Path==2, MacDst==SF1 | Push VLAN ID 1000,       |
|                          |                          | Port=SF1                 |
+--------------------------+--------------------------+--------------------------+
| 246                      | RSP Path==2              | Push MPLS Label 100,     |
|                          |                          | Port=Ingress             |
+--------------------------+--------------------------+--------------------------+
| 5                        | Match Any                | Drop                     |
+--------------------------+--------------------------+--------------------------+

Table: Table Transport Egress

Administering SFCOFL2
~~~~~~~~~~~~~~~~~~~~~

To use the SFC OpenFlow Renderer Karaf, at least the following Karaf
features must be installed.

-  odl-openflowplugin-all

-  odl-sfc-core (includes odl-sfc-provider and odl-sfc-model)

-  odl-sfcofl2

-  odl-sfc-ui (optional)

The following command can be used to view all of the currently installed
Karaf features:

::

    opendaylight-user@root>feature:list -i

Or, pipe the command to a grep to see a subset of the currently
installed Karaf features:

::

    opendaylight-user@root>feature:list -i | grep sfc

To install a particular feature, use the Karaf ``feature:install``
command.

SFCOFL2 Tutorial
~~~~~~~~~~~~~~~~

Overview
^^^^^^^^

The following Network Topology diagram shows how to configure SFC to
create a Service Chain.

.. figure:: ./images/sfc/sfcofl2_architecture_nwtopo.jpg
   :alt: SFC OpenFlow Renderer Typical Network Topology

   SFC OpenFlow Renderer Typical Network Topology

Prerequisites
^^^^^^^^^^^^^

To use this example, SFF OpenFlow switches must be created and connected
as illustrated above. Additionally, The SFs must be created and
connected to the SFFs.

Target Environment
^^^^^^^^^^^^^^^^^^

The target environment is not important, but this use-case was created
and only tested on Linux.

Instructions
^^^^^^^^^^^^

The steps to use this tutorial are as follows. The referenced
configuration in the steps is listed in the following sections.

There are numerous ways to send the configuration. The following
configuration chapters, the appropriate ``curl`` command is shown for
each configuration to be sent, including the URL.

Steps to configure the SFCOFL2 tutorial:

1. Send the ``SF`` RESTCONF configuration

2. Send the ``SFF`` RESTCONF configuration

3. Send the ``SFC`` RESTCONF configuration

4. Send the ``SFP`` RESTCONF configuration

5. Create the ``RSP`` with a RESTCONF RPC command

Once the configuration has been successfully created, query the Rendered
Service Paths with either the SFC UI or via RESTCONF. Notice that the
RSP is symetrical, so the following 2 RSPs will be created:

-  sfc-path1

-  sfc-path1-Reverse

At this point the Service Chains have been created, and the OpenFlow
Switches are programmed to steer traffic through the Service Chain.
Traffic can now be injected from a client into the Service Chain. To
debug problems, the OpenFlow tables can be dumped with the following
commands, assuming SFF1 is called ``s1`` and SFF2 is called ``s2``.

::

    sudo ovs-ofctl -O OpenFlow13  dump-flows s1

::

    sudo ovs-ofctl -O OpenFlow13  dump-flows s2

In all the following configuration sections, replace the ``${JSON}``
string with the appropriate JSON configuration. Also, change the
``localhost`` desintation in the URL accordingly.

Service Function configuration
''''''''''''''''''''''''''''''

The Service Function configuration can be sent with the following
command:

::

    curl -i -H "Content-Type: application/json" -H "Cache-Control: no-cache" --data '${JSON}' -X PUT --user admin:admin http://localhost:8181/restconf/config/service-function:service-functions/

**SF configuration JSON.**

::

    {
     "service-functions": {
       "service-function": [
         {
           "name": "sf1",
           "type": "service-function-type:http-header-enrichment",
           "nsh-aware": false,
           "ip-mgmt-address": "10.0.0.2",
           "sf-data-plane-locator": [
             {
               "name": "sf1-sff1",
               "mac": "00:00:08:01:02:01",
               "vlan-id": 1000,
               "transport": "service-locator:mac",
               "service-function-forwarder": "sff1"
             }
           ]
         },
         {
           "name": "sf2",
           "type": "service-function-type:firewall",
           "nsh-aware": false,
           "ip-mgmt-address": "10.0.0.3",
           "sf-data-plane-locator": [
             {
               "name": "sf2-sff2",
               "mac": "00:00:08:01:03:01",
               "vlan-id": 2000,
               "transport": "service-locator:mac",
               "service-function-forwarder": "sff2"
             }
           ]
         }
       ]
     }
    }

Service Function Forwarder configuration
''''''''''''''''''''''''''''''''''''''''

The Service Function Forwarder configuration can be sent with the
following command:

::

    curl -i -H "Content-Type: application/json" -H "Cache-Control: no-cache" --data '${JSON}' -X PUT --user admin:admin http://localhost:8181/restconf/config/service-function-forwarder:service-function-forwarders/

**SFF configuration JSON.**

::

    {
     "service-function-forwarders": {
       "service-function-forwarder": [
         {
           "name": "sff1",
           "service-node": "openflow:2",
           "sff-data-plane-locator": [
             {
               "name": "ulSff1Ingress",
               "data-plane-locator":
               {
                   "mpls-label": 100,
                   "transport": "service-locator:mpls"
               },
               "service-function-forwarder-ofs:ofs-port":
               {
                   "mac": "11:11:11:11:11:11",
                   "port-id" : "1"
               }
             },
             {
               "name": "ulSff1ToSff2",
               "data-plane-locator":
               {
                   "mpls-label": 101,
                   "transport": "service-locator:mpls"
               },
               "service-function-forwarder-ofs:ofs-port":
               {
                   "mac": "33:33:33:33:33:33",
                   "port-id" : "2"
               }
             }
           ],
           "service-function-dictionary": [
             {
               "name": "sf1",
               "type": "service-function-type:http-header-enrichment",
               "sff-sf-data-plane-locator":
               {
                   "mac": "22:22:22:22:22:22",
                   "vlan-id": 1000,
                   "transport": "service-locator:mac"
               },
               "service-function-forwarder-ofs:ofs-port":
               {
                   "port-id" : "3"
               }
             }
           ]
         },
         {
           "name": "sff2",
           "service-node": "openflow:3",
           "sff-data-plane-locator": [
             {
               "name": "ulSff2Ingress",
               "data-plane-locator":
               {
                   "mpls-label": 101,
                   "transport": "service-locator:mpls"
               },
               "service-function-forwarder-ofs:ofs-port":
               {
                   "mac": "44:44:44:44:44:44",
                   "port-id" : "1"
               }
             },
             {
               "name": "ulSff2Egress",
               "data-plane-locator":
               {
                   "mpls-label": 102,
                   "transport": "service-locator:mpls"
               },
               "service-function-forwarder-ofs:ofs-port":
               {
                   "mac": "66:66:66:66:66:66",
                   "port-id" : "2"
               }
             }
           ],
           "service-function-dictionary": [
             {
               "name": "sf2",
               "type": "service-function-type:firewall",
               "sff-sf-data-plane-locator":
               {
                   "mac": "55:55:55:55:55:55",
                   "vlan-id": 2000,
                   "transport": "service-locator:mac"
               },
               "service-function-forwarder-ofs:ofs-port":
               {
                   "port-id" : "3"
               }
             }
           ]
         }
       ]
     }
    }

Service Function Chain configuration
''''''''''''''''''''''''''''''''''''

The Service Function Chain configuration can be sent with the following
command:

::

    curl -i -H "Content-Type: application/json" -H "Cache-Control: no-cache" --data '${JSON}' -X PUT --user admin:admin http://localhost:8181/restconf/config/service-function-chain:service-function-chains/

**SFC configuration JSON.**

::

    {
     "service-function-chains": {
       "service-function-chain": [
         {
           "name": "sfc-chain1",
           "symmetric": true,
           "sfc-service-function": [
             {
               "name": "hdr-enrich-abstract1",
               "type": "service-function-type:http-header-enrichment"
             },
             {
               "name": "firewall-abstract1",
               "type": "service-function-type:firewall"
             }
           ]
         }
       ]
     }
    }

Service Function Path configuration
'''''''''''''''''''''''''''''''''''

The Service Function Path configuration can be sent with the following
command:

::

    curl -i -H "Content-Type: application/json" -H "Cache-Control: no-cache" --data '${JSON}' -X PUT --user admin:admin http://localhost:8181/restconf/config/service-function-path:service-function-paths/

**SFP configuration JSON.**

::

    {
      "service-function-paths": {
        "service-function-path": [
          {
            "name": "sfc-path1",
            "service-chain-name": "sfc-chain1",
            "transport-type": "service-locator:mpls",
            "symmetric": true
          }
        ]
      }
    }

Rendered Service Path creation
''''''''''''''''''''''''''''''

::

    curl -i -H "Content-Type: application/json" -H "Cache-Control: no-cache" --data '${JSON}' -X POST --user admin:admin http://localhost:8181/restconf/operations/rendered-service-path:create-rendered-path/

**RSP creation JSON.**

::

    {
     "input": {
         "name": "sfc-path1",
         "parent-service-function-path": "sfc-path1",
         "symmetric": true
     }
    }

Rendered Service Path removal
'''''''''''''''''''''''''''''

The following command can be used to remove a Rendered Service Path
called ``sfc-path1``:

::

    curl -i -H "Content-Type: application/json" -H "Cache-Control: no-cache" --data '{"input": {"name": "sfc-path1" } }' -X POST --user admin:admin http://localhost:8181/restconf/operations/rendered-service-path:delete-rendered-path/

Rendered Service Path Query
'''''''''''''''''''''''''''

The following command can be used to query all of the created Rendered
Service Paths:

::

    curl -H "Content-Type: application/json" -H "Cache-Control: no-cache" -X GET --user admin:admin http://localhost:8181/restconf/operational/rendered-service-path:rendered-service-paths/

Service Function Scheduling Algorithms
--------------------------------------

Overview
~~~~~~~~

When creating the Rendered Service Path, the origin SFC controller chose
the first available service function from a list of service function
names. This may result in many issues such as overloaded service
functions and a longer service path as SFC has no means to understand
the status of service functions and network topology. The service
function selection framework supports at least four algorithms (Random,
Round Robin, Load Balancing and Shortest Path) to select the most
appropriate service function when instantiating the Rendered Service
Path. In addition, it is an extensible framework that allows 3rd party
selection algorithm to be plugged in.

Architecture
~~~~~~~~~~~~

The following figure illustrates the service function selection
framework and algorithms.

.. figure:: ./images/sfc/sf-selection-arch.png
   :alt: SF Selection Architecture

   SF Selection Architecture

A user has three different ways to select one service function selection
algorithm:

1. Integrated RESTCONF Calls. OpenStack and/or other administration
   system could provide plugins to call the APIs to select one
   scheduling algorithm.

2. Command line tools. Command line tools such as curl or browser
   plugins such as POSTMAN (for Google Chrome) and RESTClient (for
   Mozilla Firefox) could select schedule algorithm by making RESTCONF
   calls.

3. SFC-UI. Now the SFC-UI provides an option for choosing a selection
   algorithm when creating a Rendered Service Path.

The RESTCONF northbound SFC API provides GUI/RESTCONF interactions for
choosing the service function selection algorithm. MD-SAL data store
provides all supported service function selection algorithms, and
provides APIs to enable one of the provided service function selection
algorithms. Once a service function selection algorithm is enabled, the
service function selection algorithm will work when creating a Rendered
Service Path.

Select SFs with Scheduler
~~~~~~~~~~~~~~~~~~~~~~~~~

Administrator could use both the following ways to select one of the
selection algorithm when creating a Rendered Service Path.

-  Command line tools. Command line tools includes Linux commands curl
   or even browser plugins such as POSTMAN(for Google Chrome) or
   RESTClient(for Mozilla Firefox). In this case, the following JSON
   content is needed at the moment:
   Service\_function\_schudule\_type.json

   ::

       {
         "service-function-scheduler-types": {
           "service-function-scheduler-type": [
             {
               "name": "random",
               "type": "service-function-scheduler-type:random",
               "enabled": false
             },
             {
               "name": "roundrobin",
               "type": "service-function-scheduler-type:round-robin",
               "enabled": true
             },
             {
               "name": "loadbalance",
               "type": "service-function-scheduler-type:load-balance",
               "enabled": false
             },
             {
               "name": "shortestpath",
               "type": "service-function-scheduler-type:shortest-path",
               "enabled": false
             }
           ]
         }
       }

   If using the Linux curl command, it could be:

   ::

       curl -i -H "Content-Type: application/json" -H "Cache-Control: no-cache" --data '$${Service_function_schudule_type.json}'
       -X PUT --user admin:admin http://localhost:8181/restconf/config/service-function-scheduler-type:service-function-scheduler-types/

   Here is also a snapshot for using the RESTClient plugin:

.. figure:: ./images/sfc/RESTClient-snapshot.png
   :alt: Mozilla Firefox RESTClient

   Mozilla Firefox RESTClient

-  SFC-UI.SFC-UI provides a drop down menu for service function
   selection algorithm. Here is a snapshot for the user interaction from
   SFC-UI when creating a Rendered Service Path.

.. figure:: ./images/sfc/karaf-webui-select-a-type.png
   :alt: Karaf Web UI

   Karaf Web UI

    **Note**

    Some service function selection algorithms in the drop list are not
    implemented yet. Only the first three algorithms are committed at
    the moment.

Random
^^^^^^

Select Service Function from the name list randomly.

Overview
''''''''

The Random algorithm is used to select one Service Function from the
name list which it gets from the Service Function Type randomly.

Prerequisites
'''''''''''''

-  Service Function information are stored in datastore.

-  Either no algorithm or the Random algorithm is selected.

Target Environment
''''''''''''''''''

The Random algorithm will work either no algorithm type is selected or
the Random algorithm is selected.

Instructions
''''''''''''

Once the plugins are installed into Karaf successfully, a user can use
his favorite method to select the Random scheduling algorithm type.
There are no special instructions for using the Random algorithm.

Round Robin
^^^^^^^^^^^

Select Service Function from the name list in Round Robin manner.

Overview
''''''''

The Round Robin algorithm is used to select one Service Function from
the name list which it gets from the Service Function Type in a Round
Robin manner, this will balance workloads to all Service Functions.
However, this method cannot help all Service Functions load the same
workload because it’s flow-based Round Robin.

Prerequisites
'''''''''''''

-  Service Function information are stored in datastore.

-  Round Robin algorithm is selected

Target Environment
''''''''''''''''''

The Round Robin algorithm will work one the Round Robin algorithm is
selected.

Instructions
''''''''''''

Once the plugins are installed into Karaf successfully, a user can use
his favorite method to select the Round Robin scheduling algorithm type.
There are no special instructions for using the Round Robin algorithm.

Load Balance Algorithm
^^^^^^^^^^^^^^^^^^^^^^

Select appropriate Service Function by actual CPU utilization.

Overview
''''''''

The Load Balance Algorithm is used to select appropriate Service
Function by actual CPU utilization of service functions. The CPU
utilization of service function obtained from monitoring information
reported via NETCONF.

Prerequisites
'''''''''''''

-  CPU-utilization for Service Function.

-  NETCONF server.

-  NETCONF client.

-  Each VM has a NETCONF server and it could work with NETCONF client
   well.

Instructions
''''''''''''

Set up VMs as Service Functions. enable NETCONF server in VMs. Ensure
that you specify them separately. For example:

a. Set up 4 VMs include 2 SFs' type are Firewall, Others are Napt44.
   Name them as firewall-1, firewall-2, napt44-1, napt44-2 as Service
   Function. The four VMs can run either the same server or different
   servers.

b. Install NETCONF server on every VM and enable it. More information on
   NETCONF can be found on the OpenDaylight wiki here:
   https://wiki.opendaylight.org/view/OpenDaylight_Controller:Config:Examples:Netconf:Manual_netopeer_installation

c. Get Monitoring data from NETCONF server. These monitoring data should
   be get from the NETCONF server which is running in VMs. The following
   static XML data is an example:

static XML data like this:

::

    <?xml version="1.0" encoding="UTF-8"?>
    <service-function-description-monitor-report>
      <SF-description>
        <number-of-dataports>2</number-of-dataports>
        <capabilities>
          <supported-packet-rate>5</supported-packet-rate>
          <supported-bandwidth>10</supported-bandwidth>
          <supported-ACL-number>2000</supported-ACL-number>
          <RIB-size>200</RIB-size>
          <FIB-size>100</FIB-size>
          <ports-bandwidth>
            <port-bandwidth>
              <port-id>1</port-id>
              <ipaddress>10.0.0.1</ipaddress>
              <macaddress>00:1e:67:a2:5f:f4</macaddress>
              <supported-bandwidth>20</supported-bandwidth>
            </port-bandwidth>
            <port-bandwidth>
              <port-id>2</port-id>
              <ipaddress>10.0.0.2</ipaddress>
              <macaddress>01:1e:67:a2:5f:f6</macaddress>
              <supported-bandwidth>10</supported-bandwidth>
            </port-bandwidth>
          </ports-bandwidth>
        </capabilities>
      </SF-description>
      <SF-monitoring-info>
        <liveness>true</liveness>
        <resource-utilization>
            <packet-rate-utilization>10</packet-rate-utilization>
            <bandwidth-utilization>15</bandwidth-utilization>
            <CPU-utilization>12</CPU-utilization>
            <memory-utilization>17</memory-utilization>
            <available-memory>8</available-memory>
            <RIB-utilization>20</RIB-utilization>
            <FIB-utilization>25</FIB-utilization>
            <power-utilization>30</power-utilization>
            <SF-ports-bandwidth-utilization>
              <port-bandwidth-utilization>
                <port-id>1</port-id>
                <bandwidth-utilization>20</bandwidth-utilization>
              </port-bandwidth-utilization>
              <port-bandwidth-utilization>
                <port-id>2</port-id>
                <bandwidth-utilization>30</bandwidth-utilization>
              </port-bandwidth-utilization>
            </SF-ports-bandwidth-utilization>
        </resource-utilization>
      </SF-monitoring-info>
    </service-function-description-monitor-report>

a. Unzip SFC release tarball.

b. Run SFC: ${sfc}/bin/karaf. More information on Service Function
   Chaining can be found on the OpenDaylight SFC’s wiki page:
   https://wiki.opendaylight.org/view/Service_Function_Chaining:Main

a. Deploy the SFC2 (firewall-abstract2⇒napt44-abstract2) and click
   button to Create Rendered Service Path in SFC UI
   (http://localhost:8181/sfc/index.html).

b. Verify the Rendered Service Path to ensure the CPU utilization of the
   selected hop is the minimum one among all the service functions with
   same type. The correct RSP is firewall-1⇒napt44-2

Shortest Path Algorithm
^^^^^^^^^^^^^^^^^^^^^^^

Select appropriate Service Function by Dijkstra’s algorithm. Dijkstra’s
algorithm is an algorithm for finding the shortest paths between nodes
in a graph.

Overview
''''''''

The Shortest Path Algorithm is used to select appropriate Service
Function by actual topology.

Prerequisites
'''''''''''''

-  Depolyed topology (include SFFs, SFs and their links).

-  Dijkstra’s algorithm. More information on Dijkstra’s algorithm can be
   found on the wiki here:
   http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

Instructions
''''''''''''

a. Unzip SFC release tarball.

b. Run SFC: ${sfc}/bin/karaf.

c. Depoly SFFs and SFs. import the service-function-forwarders.json and
   service-functions.json in UI
   (http://localhost:8181/sfc/index.html#/sfc/config)

service-function-forwarders.json:

::

    {
      "service-function-forwarders": {
        "service-function-forwarder": [
          {
            "name": "SFF-br1",
            "service-node": "OVSDB-test01",
            "rest-uri": "http://localhost:5001",
            "sff-data-plane-locator": [
              {
                "name": "eth0",
                "service-function-forwarder-ovs:ovs-bridge": {
                  "uuid": "4c3778e4-840d-47f4-b45e-0988e514d26c",
                  "bridge-name": "br-tun"
                },
                "data-plane-locator": {
                  "port": 5000,
                  "ip": "192.168.1.1",
                  "transport": "service-locator:vxlan-gpe"
                }
              }
            ],
            "service-function-dictionary": [
              {
                "sff-sf-data-plane-locator": {
                  "port": 10001,
                  "ip": "10.3.1.103"
                },
                "name": "napt44-1",
                "type": "service-function-type:napt44"
              },
              {
                "sff-sf-data-plane-locator": {
                  "port": 10003,
                  "ip": "10.3.1.102"
                },
                "name": "firewall-1",
                "type": "service-function-type:firewall"
              }
            ],
            "connected-sff-dictionary": [
              {
                "name": "SFF-br3"
              }
            ]
          },
          {
            "name": "SFF-br2",
            "service-node": "OVSDB-test01",
            "rest-uri": "http://localhost:5002",
            "sff-data-plane-locator": [
              {
                "name": "eth0",
                "service-function-forwarder-ovs:ovs-bridge": {
                  "uuid": "fd4d849f-5140-48cd-bc60-6ad1f5fc0a1",
                  "bridge-name": "br-tun"
                },
                "data-plane-locator": {
                  "port": 5000,
                  "ip": "192.168.1.2",
                  "transport": "service-locator:vxlan-gpe"
                }
              }
            ],
            "service-function-dictionary": [
              {
                "sff-sf-data-plane-locator": {
                  "port": 10002,
                  "ip": "10.3.1.103"
                },
                "name": "napt44-2",
                "type": "service-function-type:napt44"
              },
              {
                "sff-sf-data-plane-locator": {
                  "port": 10004,
                  "ip": "10.3.1.101"
                },
                "name": "firewall-2",
                "type": "service-function-type:firewall"
              }
            ],
            "connected-sff-dictionary": [
              {
                "name": "SFF-br3"
              }
            ]
          },
          {
            "name": "SFF-br3",
            "service-node": "OVSDB-test01",
            "rest-uri": "http://localhost:5005",
            "sff-data-plane-locator": [
              {
                "name": "eth0",
                "service-function-forwarder-ovs:ovs-bridge": {
                  "uuid": "fd4d849f-5140-48cd-bc60-6ad1f5fc0a4",
                  "bridge-name": "br-tun"
                },
                "data-plane-locator": {
                  "port": 5000,
                  "ip": "192.168.1.2",
                  "transport": "service-locator:vxlan-gpe"
                }
              }
            ],
            "service-function-dictionary": [
              {
                "sff-sf-data-plane-locator": {
                  "port": 10005,
                  "ip": "10.3.1.104"
                },
                "name": "test-server",
                "type": "service-function-type:dpi"
              },
              {
                "sff-sf-data-plane-locator": {
                  "port": 10006,
                  "ip": "10.3.1.102"
                },
                "name": "test-client",
                "type": "service-function-type:dpi"
              }
            ],
            "connected-sff-dictionary": [
              {
                "name": "SFF-br1"
              },
              {
                "name": "SFF-br2"
              }
            ]
          }
        ]
      }
    }

service-functions.json:

::

    {
      "service-functions": {
        "service-function": [
          {
            "rest-uri": "http://localhost:10001",
            "ip-mgmt-address": "10.3.1.103",
            "sf-data-plane-locator": [
              {
                "name": "preferred",
                "port": 10001,
                "ip": "10.3.1.103",
                "service-function-forwarder": "SFF-br1"
              }
            ],
            "name": "napt44-1",
            "type": "service-function-type:napt44",
            "nsh-aware": true
          },
          {
            "rest-uri": "http://localhost:10002",
            "ip-mgmt-address": "10.3.1.103",
            "sf-data-plane-locator": [
              {
                "name": "master",
                "port": 10002,
                "ip": "10.3.1.103",
                "service-function-forwarder": "SFF-br2"
              }
            ],
            "name": "napt44-2",
            "type": "service-function-type:napt44",
            "nsh-aware": true
          },
          {
            "rest-uri": "http://localhost:10003",
            "ip-mgmt-address": "10.3.1.103",
            "sf-data-plane-locator": [
              {
                "name": "1",
                "port": 10003,
                "ip": "10.3.1.102",
                "service-function-forwarder": "SFF-br1"
              }
            ],
            "name": "firewall-1",
            "type": "service-function-type:firewall",
            "nsh-aware": true
          },
          {
            "rest-uri": "http://localhost:10004",
            "ip-mgmt-address": "10.3.1.103",
            "sf-data-plane-locator": [
              {
                "name": "2",
                "port": 10004,
                "ip": "10.3.1.101",
                "service-function-forwarder": "SFF-br2"
              }
            ],
            "name": "firewall-2",
            "type": "service-function-type:firewall",
            "nsh-aware": true
          },
          {
            "rest-uri": "http://localhost:10005",
            "ip-mgmt-address": "10.3.1.103",
            "sf-data-plane-locator": [
              {
                "name": "3",
                "port": 10005,
                "ip": "10.3.1.104",
                "service-function-forwarder": "SFF-br3"
              }
            ],
            "name": "test-server",
            "type": "service-function-type:dpi",
            "nsh-aware": true
          },
          {
            "rest-uri": "http://localhost:10006",
            "ip-mgmt-address": "10.3.1.103",
            "sf-data-plane-locator": [
              {
                "name": "4",
                "port": 10006,
                "ip": "10.3.1.102",
                "service-function-forwarder": "SFF-br3"
              }
            ],
            "name": "test-client",
            "type": "service-function-type:dpi",
            "nsh-aware": true
          }
        ]
      }
    }

The depolyed topology like this:

::

                  +----+           +----+          +----+
                  |sff1|+----------|sff3|---------+|sff2|
                  +----+           +----+          +----+
                    |                                  |
             +--------------+                   +--------------+
             |              |                   |              |
        +----------+   +--------+          +----------+   +--------+
        |firewall-1|   |napt44-1|          |firewall-2|   |napt44-2|
        +----------+   +--------+          +----------+   +--------+

-  Deploy the SFC2(firewall-abstract2⇒napt44-abstract2), select
   "Shortest Path" as schedule type and click button to Create Rendered
   Service Path in SFC UI (http://localhost:8181/sfc/index.html).

.. figure:: ./images/sfc/sf-schedule-type.png
   :alt: select schedule type

   select schedule type

-  Verify the Rendered Service Path to ensure the selected hops are
   linked in one SFF. The correct RSP is firewall-1⇒napt44-1 or
   firewall-2⇒napt44-2. The first SF type is Firewall in Service
   Function Chain. So the algorithm will select first Hop randomly among
   all the SFs type is Firewall. Assume the first selected SF is
   firewall-2. All the path from firewall-1 to SF which type is Napt44
   are list:

   -  Path1: firewall-2 → sff2 → napt44-2

   -  Path2: firewall-2 → sff2 → sff3 → sff1 → napt44-1 The shortest
      path is Path1, so the selected next hop is napt44-2.

.. figure:: ./images/sfc/sf-rendered-service-path.png
   :alt: rendered service path

   rendered service path

Service Function Load Balancing User Guide
------------------------------------------

Overview
~~~~~~~~

SFC Load-Balancing feature implements load balancing of Service
Functions, rather than a one-to-one mapping between
Service-Function-Forwarder and Service-Function.

Load Balancing Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Service Function Groups (SFG) can replace Service Functions (SF) in the
Rendered Path model. A Service Path can only be defined using SFGs or
SFs, but not a combination of both.

Relevant objects in the YANG model are as follows:

1. Service-Function-Group-Algorithm:

   ::

       Service-Function-Group-Algorithms {
           Service-Function-Group-Algorithm {
               String name
               String type
           }
       }

   ::

       Available types: ALL, SELECT, INDIRECT, FAST_FAILURE

2. Service-Function-Group:

   ::

       Service-Function-Groups {
           Service-Function-Group {
               String name
               String serviceFunctionGroupAlgorithmName
               String type
               String groupId
               Service-Function-Group-Element {
                   String service-function-name
                   int index
               }
           }
       }

3. ServiceFunctionHop: holds a reference to a name of SFG (or SF)

Tutorials
~~~~~~~~~

This tutorial will explain how to create a simple SFC configuration,
with SFG instead of SF. In this example, the SFG will include two
existing SF.

Setup SFC
^^^^^^^^^

For general SFC setup and scenarios, please see the SFC wiki page:
https://wiki.opendaylight.org/view/Service_Function_Chaining:Main#SFC_101

Create an algorithm
^^^^^^^^^^^^^^^^^^^

POST -
http://127.0.0.1:8181/restconf/config/service-function-group-algorithm:service-function-group-algorithms

::

    {
        "service-function-group-algorithm": [
          {
            "name": "alg1"
            "type": "ALL"
          }
       ]
    }

(Header "content-type": application/json)

Verify: get all algorithms
^^^^^^^^^^^^^^^^^^^^^^^^^^

GET -
http://127.0.0.1:8181/restconf/config/service-function-group-algorithm:service-function-group-algorithms

In order to delete all algorithms: DELETE -
http://127.0.0.1:8181/restconf/config/service-function-group-algorithm:service-function-group-algorithms

Create a group
^^^^^^^^^^^^^^

POST -
http://127.0.0.1:8181/restconf/config/service-function-group:service-function-groups

::

    {
        "service-function-group": [
        {
            "rest-uri": "http://localhost:10002",
            "ip-mgmt-address": "10.3.1.103",
            "algorithm": "alg1",
            "name": "SFG1",
            "type": "service-function-type:napt44",
            "sfc-service-function": [
                {
                    "name":"napt44-104"
                },
                {
                    "name":"napt44-103-1"
                }
            ]
          }
        ]
    }

Verify: get all SFG’s
^^^^^^^^^^^^^^^^^^^^^

GET -
http://127.0.0.1:8181/restconf/config/service-function-group:service-function-groups

SNMP Plugin User Guide
======================

Installing Feature
------------------

The SNMP Plugin can be installed using a single karaf feature:
**odl-snmp-plugin**

After starting Karaf:

-  Install the feature: **feature:install odl-snmp-plugin**

-  Expose the northbound API: **feature:install odl-restconf**

Northbound APIs
---------------

There are two exposed northbound APIs: snmp-get & snmp-set

SNMP GET
~~~~~~~~

Default URL: http://localhost:8181/restconf/operations/snmp:snmp-get

POST Input
^^^^^^^^^^

+----------------+----------------+----------------+----------------+----------------+
| Field Name     | Type           | Description    | Example        | Required?      |
+================+================+================+================+================+
| ip-address     | Ipv4 Address   | The IPv4       | 10.86.3.13     | Yes            |
|                |                | Address of the |                |                |
|                |                | desired        |                |                |
|                |                | network node   |                |                |
+----------------+----------------+----------------+----------------+----------------+
| oid            | String         | The Object     | 1.3.6.1.2.1.1. | Yes            |
|                |                | Identifier of  | 1              |                |
|                |                | the desired    |                |                |
|                |                | MIB            |                |                |
|                |                | table/object   |                |                |
+----------------+----------------+----------------+----------------+----------------+
| get-type       | ENUM (GET,     | The type of    | GET-BULK       | Yes            |
|                | GET-NEXT,      | get request to |                |                |
|                | GET-BULK,      | send           |                |                |
|                | GET-WALK)      |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| community      | String         | The community  | private        | No. (Default:  |
|                |                | string to use  |                | public)        |
|                |                | for the SNMP   |                |                |
|                |                | request        |                |                |
+----------------+----------------+----------------+----------------+----------------+

**Example.**

::

     {
         "input": {
             "ip-address": "10.86.3.13",
             "oid" : "1.3.6.1.2.1.1.1",
             "get-type" : "GET-BULK",
             "community" : "private"
         }
     }

POST Output
^^^^^^^^^^^

+--------------------------+--------------------------+--------------------------+
| Field Name               | Type                     | Description              |
+==========================+==========================+==========================+
| results                  | List of { "value" :      | The results of the SNMP  |
|                          | String } pairs           | query                    |
+--------------------------+--------------------------+--------------------------+

**Example.**

::

     {
         "snmp:results": [
             {
                 "value": "Ethernet0/0/0",
                 "oid": "1.3.6.1.2.1.2.2.1.2.1"
             },
             {
                 "value": "FastEthernet0/0/0",
                 "oid": "1.3.6.1.2.1.2.2.1.2.2"
             },
             {
                 "value": "GigabitEthernet0/0/0",
                 "oid": "1.3.6.1.2.1.2.2.1.2.3"
             }
         ]
     }

SNMP SET
~~~~~~~~

Default URL: http://localhost:8181/restconf/operations/snmp:snmp-set

POST Input
^^^^^^^^^^

+----------------+----------------+----------------+----------------+----------------+
| Field Name     | Type           | Description    | Example        | Required?      |
+================+================+================+================+================+
| ip-address     | Ipv4 Address   | The Ipv4       | 10.86.3.13     | Yes            |
|                |                | address of the |                |                |
|                |                | desired        |                |                |
|                |                | network node   |                |                |
+----------------+----------------+----------------+----------------+----------------+
| oid            | String         | The Object     | 1.3.6.2.1.1.1  | Yes            |
|                |                | Identifier of  |                |                |
|                |                | the desired    |                |                |
|                |                | MIB object     |                |                |
+----------------+----------------+----------------+----------------+----------------+
| value          | String         | The value to   | "Hello World"  | Yes            |
|                |                | set on the     |                |                |
|                |                | network device |                |                |
+----------------+----------------+----------------+----------------+----------------+
| community      | String         | The community  | private        | No. (Default:  |
|                |                | string to use  |                | public)        |
|                |                | for the SNMP   |                |                |
|                |                | request        |                |                |
+----------------+----------------+----------------+----------------+----------------+

**Example.**

::

     {
         "input": {
             "ip-address": "10.86.3.13",
             "oid" : "1.3.6.1.2.1.1.1.0",
             "value" : "Sample description",
             "community" : "private"
         }
     }

POST Output
^^^^^^^^^^^

On a successful SNMP-SET, no output is presented, just a HTTP status of
200.

Errors
^^^^^^

If any errors happen in the set request, you will be presented with an
error message in the output.

For example, on a failed set request you may see an error like:

::

     {
         "errors": {
             "error": [
                 {
                     "error-type": "application",
                     "error-tag": "operation-failed",
                     "error-message": "SnmpSET failed with error status: 17, error index: 1. StatusText: Not writable"
                 }
             ]
         }
     }

which corresponds to Error status 17 in the SNMPv2 RFC:
https://tools.ietf.org/html/rfc1905.

SXP User Guide
==============

Overview
--------

SXP (Source-Group Tag eXchange Protocol) project is an effort to enhance
OpenDaylight platform with IP-SGT (IP Address to Source Group Tag)
bindings that can be learned from connected SXP-aware network nodes. The
current implementation supports SXP protocol version 4 according to the
Smith, Kandula - SXP `IETF
draft <https://tools.ietf.org/html/draft-smith-kandula-sxp-04>`__ and
grouping of peers and creating filters based on ACL/Prefix-list syntax
for filtering outbound and inbound IP-SGT bindings. All protocol legacy
versions 1-3 are supported as well. Additionally, version 4 adds
bidirectional connection type as an extension of a unidirectional one.

SXP Architecture
----------------

The SXP Server manages all connected clients in separate threads and a
common SXP protocol agreement is used between connected peers. Each SXP
network peer is modelled with its pertaining class, e.g., SXP Server
represents the SXP Speaker, SXP Listener the Client. The server program
creates the ServerSocket object on a specified port and waits until a
client starts up and requests connect on the IP address and port of the
server. The client program opens a Socket that is connected to the
server running on the specified host IP address and port.

The SXP Listener maintains connection with its speaker peer. From an
opened channel pipeline, all incoming SXP messages are processed by
various handlers. Message must be decoded, parsed and validated.

The SXP Speaker is a counterpart to the SXP Listener. It maintains a
connection with its listener peer and sends composed messages.

The SXP Binding Handler extracts the IP-SGT binding from a message and
pulls it into the SXP-Database. If an error is detected during the
IP-SGT extraction, an appropriate error code and sub-code is selected
and an error message is sent back to the connected peer. All transitive
messages are routed directly to the output queue of SXP Binding
Dispatcher.

The IP-SGT Manager handles bindings from multiple connections. If a new
data has been added into or deleted from the SXP-Database, or binding’s
contributor change is detected, the manager performs an arbitration
process above the SXP-Database to resolve the binding duplicity and
prevent possible information loops. Finally, it updates the
IP-SGT-Master database that consists only of valid and unique bindings,
i.e., a single binding per IP address.

The IP-SGT Manager also contains RPCs that can be used by other
OpenDaylight plugins, or by making REST calls, to add, update or to
delete bindings in or from the SXP-database.

The SXP Binding Dispatcher represents a selector that will decides how
many data from the SXP-database will be sent and when. It is responsible
for message content composition based on maximum message length.

The SXP Binding Filters handles filtering of outcoming and incoming
IP-SGT bindings according to BGP filtering using ACL and Prefix List
syntax for specifiing filter.

Configuring SXP
---------------

The OpenDaylight Karaf distribution comes pre-configured with baseline
SXP configuration.

-  **22-sxp-controller-one-node.xml** (defines the basic parameters)

Administering or Managing SXP
-----------------------------

By RPC (response is XML document containing requested data or operation
status):

-  Get Connections POST
   http://127.0.0.1:8181/restconf/operations/sxp-controller:get-connections

::

    <input xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     <requested-node>0.0.0.100</requested-node>
    </input>

-  Add Connection POST
   http://127.0.0.1:8181/restconf/operations/sxp-controller:add-connection

::

    <input xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     <connections>
      <connection>
       <!--vpn>vpn1</vpn-->
       <peer-address>172.20.161.50</peer-address>
       <!--source-ip></source-ip-->
       <tcp-port>64999</tcp-port>
       <!-- Password setup: default | none -->
       <password>default</password>
       <!-- Mode: speaker/listener/both -->
       <mode>speaker</mode>
       <version>version4</version>
       <description>Connection to ASR1K</description>
       <!-- Timers setup: 0 to disable specific timer usability, the default value will be used -->
       <connection-timers>
        <!-- Speaker -->
        <hold-time-min-acceptable>45</hold-time-min-acceptable>
        <keep-alive-time>30</keep-alive-time>
       </connection-timers>
      </connection>
      <connection>
       <!--vpn>vpn1</vpn-->
       <peer-address>172.20.161.178</peer-address>
       <!--source-ip></source-ip-->
       <tcp-port>64999</tcp-port>
       <!-- Password setup: default | none -->
       <password>default</password>
       <!-- Mode: speaker/listener/both -->
       <mode>listener</mode>
       <version>version4</version>
       <description>Connection to ISR</description>
       <!-- Timers setup: 0 to disable specific timer usability, the default value will be used -->
       <connection-timers>
        <!-- Listener -->
        <!-- NON-CONFIGURABLE delete-hold-down-time -->
        <reconciliation-time>120</reconciliation-time>
        <hold-time>90</hold-time>
        <hold-time-min>90</hold-time-min>
        <hold-time-max>180</hold-time-max>
       </connection-timers>
      </connection>
     </connections>
    </input>

-  Delete Connection POST
   http://127.0.0.1:8181/restconf/operations/sxp-controller:delete-connection

::

    <input xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     <peer-address>172.20.161.50</peer-address>
    </input>

-  Add Binding Entry POST
   http://127.0.0.1:8181/restconf/operations/sxp-controller:add-entry

::

    <input xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     <ip-prefix>192.168.2.1/32</ip-prefix>
     <sgt>20</sgt >
    </input>

-  Update Binding Entry POST
   http://127.0.0.1:8181/restconf/operations/sxp-controller:update-entry

::

    <input xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     <original-binding>
      <ip-prefix>192.168.2.1/32</ip-prefix>
      <sgt>20</sgt>
     </original-binding>
     <new-binding>
      <ip-prefix>192.168.3.1/32</ip-prefix>
      <sgt>30</sgt>
     </new-binding>
    </input>

-  Delete Binding Entry POST
   http://127.0.0.1:8181/restconf/operations/sxp-controller:delete-entry

::

    <input xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     <ip-prefix>192.168.3.1/32</ip-prefix>
     <sgt>30</sgt >
    </input>

-  Get Node Bindings

   This RPC gets particular device bindings. An SXP-aware node is
   identified with a unique Node-ID. If a user requests bindings for a
   Speaker 20.0.0.2, the RPC will search for an appropriate path, which
   contains 20.0.0.2 Node-ID, within locally learnt SXP data in the SXP
   database and replies with associated bindings. POST
   http://127.0.0.1:8181/restconf/operations/sxp-controller:get-node-bindings

::

    <input xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     <requested-node>20.0.0.2</requested-node>
    </input>

-  Get Binding SGTs POST
   http://127.0.0.1:8181/restconf/operations/sxp-controller:get-binding-sgts

::

    <input xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
     <ip-prefix>192.168.12.2/32</ip-prefix>
    </input>

Use cases for SXP
~~~~~~~~~~~~~~~~~

Cisco has a wide installed base of network devices supporting SXP. By
including SXP in OpenDaylight, the binding of policy groups to IP
addresses can be made available for possible further processing to a
wide range of devices, and applications running on OpenDaylight. The
range of applications that would be enabled is extensive. Here are just
a few of them:

OpenDaylight based applications can take advantage of the IP-SGT binding
information. For example, access control can be defined by an operator
in terms of policy groups, while OpenDaylight can configure access
control lists on network elements using IP addresses, e.g., existing
technology.

Interoperability between different vendors. Vendors have different
policy systems. Knowing the IP-SGT binding for Cisco makes it possible
to maintain policy groups between Cisco and other vendors.

OpenDaylight can aggregate the binding information from many devices and
communicate it to a network element. For example, a firewall can use the
IP-SGT binding information to know how to handle IPs based on the
group-based ACLs it has set. But to do this with SXP alone, the firewall
has to maintain a large number of network connections to get the binding
information. This incurs heavy overhead costs to maintain all of the SXP
peering and protocol information. OpenDaylight can aggregate the
IP-group information so that the firewall need only connect to
OpenDaylight. By moving the information flow outside of the network
elements to a centralized position, we reduce the overhead of the CPU
consumption on the enforcement element. This is a huge savings - it
allows the enforcement point to only have to make one connection rather
than thousands, so it can concentrate on its primary job of forwarding
and enforcing.

OpenDaylight can relay the binding information from one network element
to others. Changes in group membership can be propagated more readily
through a centralized model. For example, in a security application a
particular host (e.g., user or IP Address) may be found to be acting
suspiciously or violating established security policies. The defined
response is to put the host into a different source group for
remediation actions such as a lower quality of service, restricted
access to critical servers, or special routing conditions to ensure
deeper security enforcement (e.g., redirecting the host’s traffic
through an IPS with very restrictive policies). Updated group membership
for this host needs to be communicated to multiple network elements as
soon as possible; a very efficient and effective method of propagation
can be performed using OpenDaylight as a centralized point for relaying
the information.

OpenDayLight can create filters for exporting and recieving IP-SGTT
bindings used on specific peer groups, thus can provide more complex
maintaining of policy groups.

Although the IP-SGT binding is only one specific piece of information,
and although SXP is implemented widely in a single vendor’s equipment,
bringing the ability of OpenDaylight to process and distribute the
bindings, is a very specific immediate useful implementation of policy
groups. It would go a long way to develop both the usefulness of
OpenDaylight and of policy groups.

TCPMD5 User Guide
=================

This user guide describes the configuration for Border Gateway Protocol
(BGP) and Path Computation Element Protocol (PCEP) using MD5
authentication. It is destined for users who build applications using
MD5 library.

Overview
--------

The TCPMD5 library provides access to
`RFC-2385 <http://tools.ietf.org/html/rfc2385>`__ MD5 Signature Option
on operating systems which support it in their TCP stack. This option
has been historically used to protect BGP sessions, but is equally
useful for protecting PCEP sessions.

    **Important**

    **Before you continue with steps in this user guide, make sure BGP
    and/or PCEP is configured properly.**

TCPMD5 authentication is **disabled** by default. To enable it (for both
protocols), uncomment the contents of *20-tcpmd5.xml*. You can find this
configuration file in your OpenDaylight directory
*etc/opendaylight/karaf* .

    **Caution**

    **If the connection can not be established, there are no warnings or
    errors, so be sure to double check your configuration and
    passwords.**

Configuring TCPMD5 manually
---------------------------

BGP
~~~

    **Important**

    **Make sure your *20-tcpmd5.xml* has its content uncommented.**

To enable TCPMD5 for the BGP protocol, perform the following steps:

1. In *31-bgp.xml* uncomment the TCP MD5 section:

   .. code:: xml

       <!--
        Uncomment this block to enable TCPMD5 Signature support
       -->
       <md5-channel-factory>
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">prefix:md5-channel-factory</type>
        <name>md5-client-channel-factory</name>
       </md5-channel-factory>
       <md5-server-channel-factory>
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">prefix:md5-server-channel-factory</type>
        <name>md5-server-channel-factory</name>
       </md5-server-channel-factory>

2. In *41-bgp-example.xml* add <password> tag to module
   example-bgp-peer.

   .. code:: xml

       <!--
        For TCPMD5 support, make sure the dispatcher associated with the rib has
        "md5-channel-factory" attribute set and then add a "password" attribute here.
        Note that the peer has to have the same password configured, otherwise the
        connection will not be established.
       -->
       <module>
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">prefix:bgp-peer</type>
        <name>example-bgp-peer</name>
        <host>10.25.2.27</host>
        <holdtimer>180</holdtimer>
        <rib>
         <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:cfg">prefix:rib</type>
         <name>example-bgp-rib</name>
        </rib>
        <advertized-table>
         <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">prefix:bgp-table-type</type>
         <name>ipv4-unicast</name>
        </advertized-table>
        <advertized-table>
         <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">prefix:bgp-table-type</type>
         <name>ipv6-unicast</name>
        </advertized-table>
        <advertized-table>
         <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">prefix:bgp-table-type</type>
         <name>linkstate</name>
        </advertized-table>
        <password>changeme</password>
       </module>

    **Note**

    Setting a password on other BGP devices is out of scope for this
    document.

PCEP
~~~~

    **Important**

    **Make sure your *20-tcpmd5.xml* has its content uncommented.**

To enable TCPMD5 for PCE protocol, perform the following steps:

1. In *32-pcep.xml* uncomment the TCPMD5 section:

   .. code:: xml

       <!--
        Uncomment this block to enable TCPMD5 Signature support
       -->
       <md5-channel-factory>
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">prefix:md5-channel-factory</type>
         <name>md5-client-channel-factory</name>
       </md5-channel-factory>
       <md5-server-channel-factory>
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">prefix:md5-server-channel-factory</type>
         <name>md5-server-channel-factory</name>
       </md5-server-channel-factory>

2. In *39-pcep-provider.xml* uncomment following section:

   .. code:: xml

       <!--
        For TCPMD5 support make sure the dispatcher has the "md5-server-channel-factory"
        attribute set and then set the appropriate client entries here. Note that if this
        option is configured, the PCCs connecting here must have the same password,
        otherwise they will not be able to connect.
        -->
        <client>
         <address>192.0.2.2</address>
         <password>changeme</password>
        </client>

    **Important**

    **Change the <address> value to the address of PCC, the one that is
    advertized to PCE and provide password matching the one set on
    PCC.**

    **Note**

    Setting a password on PCC is out of scope for this document.

Configuring TCPMD5 through RESTCONF
-----------------------------------

    **Important**

    Before you start, make sure, you have installed features for BGP
    and/or PCEP. Install another feature, that will provide you the
    access to *restconf/config/* URLs.

.. code:: xml

    feature:install odl-netconf-connector-all

This log message indicates successful start of netconf-connector:
*Netconf connector initialized successfully*

-  To check what modules you have currently configured, check following
   link:
   http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules/

-  To check what services you have currently configured, check following
   link:
   http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:services/

These URLs are also used to POST new configuration. If you want to
change any other configuration that is listed here, make sure you
include the correct namespaces. The correct namespace for <module> is
always *urn:opendaylight:params:xml:ns:yang:controller:config*. The
namespace for any other fields can be found by finding given module in
configuration yang files.

    **Note**

    RESTCONF will tell you if some namespace is wrong.

To enable TCPMD5 for either one of the protocols, enable TCPMD5 modules
and services:

    **Caution**

    You have to make **separate** POST requests for each module/service!

\*URL:
http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules/

**POST:**

.. code:: xml

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:jni:cfg">x:native-key-access-factory</type>
     <name>global-key-access-factory</name>
    </module>

.. code:: xml

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">x:md5-client-channel-factory</type>
     <name>md5-client-channel-factory</name>
     <key-access-factory xmlns="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:cfg">x:key-access-factory</type>
      <name>global-key-access-factory</name>
     </key-access-factory>
    </module>

.. code:: xml

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">prefix:md5-server-channel-factory-impl</type>
     <name>md5-server-channel-factory</name>
     <server-key-access-factory xmlns="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:cfg">x:key-access-factory</type>
      <name>global-key-access-factory</name>
     </server-key-access-factory>
    </module>

**URL:**
http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:services/

**POST:**

.. code:: xml

    <service xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:cfg">x:key-access-factory</type>
     <instance>
      <name>global-key-access-factory</name>
      <provider>/modules/module[type='native-key-access-factory'][name='global-key-access-factory']</provider>
     </instance>
    </service>

.. code:: xml

    <service  xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">x:md5-channel-factory</type>
     <instance>
      <name>md5-client-channel-factory</name>
      <provider>/modules/module[type='md5-client-channel-factory'][name='md5-client-channel-factory']</provider>
     </instance>
    </service>

.. code:: xml

    <service xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">prefix:md5-server-channel-factory</type>
     <instance>
      <name>md5-server-channel-factory</name>
      <provider>/modules/module[type='md5-server-channel-factory-impl'][name='md5-server-channel-factory']</provider>
     </instance>
    </service>

BGP
~~~

    **Caution**

    You have to introduce modules and services mentioned in the previous
    section. Your BGP client needs to be **ALREADY** configured. Check
    User Guide for BGP.

    **Caution**

    You need to copy and paste FULL module in order to replace it. This
    guide shows you part you need to change.

1. Enabling TCPMD5 in BGP configuration:

   **URL:**
   http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules/odl-bgp-rib-impl-cfg:bgp-dispatcher-impl/global-bgp-dispatcher

**PUT:**

.. code:: xml

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:bgp-dispatcher-impl</type>
     <name>global-bgp-dispatcher</name>
     <md5-channel-factory xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">x:md5-channel-factory</type>
      <name>md5-client-channel-factory</name>
     </md5-channel-factory>
     <md5-server-channel-factory xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">x:md5-server-channel-factory</type>
      <name>md5-server-channel-factory</name>
     </md5-server-channel-factory>
     ...
    </module>

    **Caution**

    You need to copy and paste FULL module in order to replace it. This
    guide shows you part you need to change.

1. Set password:

   **URL:**
   http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules/odl-bgp-rib-impl-cfg:bgp-peer/example-bgp-peer

**PUT:**

.. code:: xml

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">x:bgp-peer</type>
     <name>example-bgp-peer</name>
     <password xmlns="urn:opendaylight:params:xml:ns:yang:controller:bgp:rib:impl">changeme</password>
     ...
    </module>

PCEP
~~~~

    **Caution**

    You have to introduce modules and services mentioned in the previous
    section.

    **Caution**

    You need to copy and paste FULL module in order to replace it. This
    guide shows you part you need to change.

1. Enable TCPMD5 in PCEP configuration:

   **URL:**
   http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules/odl-pcep-impl-cfg:pcep-dispatcher-impl/global-pcep-dispatcher

**PUT:**

.. code:: xml

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:pcep:impl">x:pcep-dispatcher-impl</type>
     <name>global-pcep-dispatcher</name>
     <md5-channel-factory xmlns="urn:opendaylight:params:xml:ns:yang:controller:pcep:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">x:md5-channel-factory</type>
      <name>md5-client-channel-factory</name>
     </md5-channel-factory>
     <md5-server-channel-factory xmlns="urn:opendaylight:params:xml:ns:yang:controller:pcep:impl">
      <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:tcpmd5:netty:cfg">x:md5-server-channel-factory</type>
      <name>md5-server-channel-factory</name>
     </md5-server-channel-factory>
     ...
    </module>

    **Caution**

    You need to copy and paste FULL module in order to replace it. This
    guide shows you part you need to change.

1. Set password:

   **URL:**
   http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules/odl-pcep-impl-cfg:pcep-topology-provider/pcep-topology

**PUT:**

.. code:: xml

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
     <type xmlns:x="urn:opendaylight:params:xml:ns:yang:controller:pcep:topology:provider">x:pcep-topology-provider</type>
     <name>pcep-topology</name>
     <client xmlns="urn:opendaylight:params:xml:ns:yang:controller:pcep:topology:provider">
      <address xmlns="urn:opendaylight:params:xml:ns:yang:controller:pcep:topology:provider">192.0.2.2</address> <!--CHANGE THE VALUE -->
      <password>changeme</password> <!--CHANGE THE VALUE -->
     </client>
     ...
    </module>

TSDR User Guide
===============

This document describes how to use HSQLDB, HBase, and Cassandra data
stores to capture time series data using Time Series Data Repository
(TSDR) features in OpenDaylight. This document contains configuration,
administration, management, usage, and troubleshooting sections for the
features.

Overview
--------

The Time Series Data Repository (TSDR) project in OpenDaylight (ODL)
creates a framework for collecting, storing, querying, and maintaining
time series data. TSDR provides the framework for plugging in proper
data collectors to collect various time series data and store the data
into TSDR Data Stores. With a common data model and generic TSDR data
persistence APIs, the user can choose various data stores to be plugged
into the TSDR persistence framework. Currently, three types of data
stores are supported: HSQLDB relational database, HBase NoSQL database,
and Cassandra NoSQL database.

With the capabilities of data collection, storage, query, aggregation,
and purging provided by TSDR, network administrators can leverage
various data driven appliations built on top of TSDR for security risk
detection, performance analysis, operational configuration optimization,
traffic engineering, and network analytics with automated intelligence.

TSDR Architecture
-----------------

TSDR has the following major components:

-  Data Collection Service

-  Data Storage Service

-  TSDR Persistence Layer with data stores as plugins

-  TSDR Data Stores

-  Data Query Service

-  Grafana integration for time series data visualization

-  Data Aggregation Service

-  Data Purging Service

The Data Collection Service handles the collection of time series data
into TSDR and hands it over to the Data Storage Service. The Data
Storage Service stores the data into TSDR through the TSDR Persistence
Layer. The TSDR Persistence Layer provides generic Service APIs allowing
various data stores to be plugged in. The Data Aggregation Service
aggregates time series fine-grained raw data into course-grained roll-up
data to control the size of the data. The Data Purging Service
periodically purges both fine-grained raw data and course-granined
aggregated data according to user-defined schedules.

We have implemented The Data Collection Service, Data Storage Service,
TSDR Persistence Layer, TSDR HSQLDB Data Store, TSDR HBase Data Store,
and TSDR Cassandra Datastore. Among these services and components, time
series data is communicated using a common TSDR data model, which is
designed and implemented for the abstraction of time series data
commonalities. With these functions, TSDR is able to collect the data
from the data sources and store them into one of the TSDR data stores:
HSQLDB Data Store, HBase Data Store or Cassandra Data Store. Besides a
simple query command from Karaf console to retrieve data from the TSDR
data stores, we also provided a Data Query Service for the user to use
REST API to query the data from the data stores. Moreover, the user can
use Grafana, which is a time series visualization tool to view the data
stored in TSDR in various charting formats.

Configuring TSDR Data Stores
----------------------------

To Configure HSQLDB Data Store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The HSQLDB based storage files get stored automatically in <karaf
install folder>/tsdr/ directory. If you want to change the default
storage location, the configuration file to change can be found in
<karaf install folder>/etc directory. The filename is
org.ops4j.datasource-metric.cfg. Change the last portion of the
url=jdbc:hsqldb:./tsdr/metric to point to different directory.

To Configure HBase Data Store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After installing HBase Server on the same machine as OpenDaylight, if
the user accepts the default configuration of the HBase Data Store, the
user can directly proceed with the installation of HBase Data Store from
Karaf console.

Optionally, the user can configure TSDR HBase Data Store following HBase
Data Store Configuration Procedure.

-  HBase Data Store Configuration Steps

   -  Open the file etc/tsdr-persistence-hbase.peroperties under karaf
      distribution directory.

   -  Edit the following parameters:

      -  HBase server name

      -  HBase server port

      -  HBase client connection pool size

      -  HBase client write buffer size

After the configuration of HBase Data Store is complete, proceed with
the installation of HBase Data Store from Karaf console.

-  HBase Data Store Installation Steps

   -  Start Karaf Console

   -  Run the following commands from Karaf Console: feature:install
      odl-tsdr-hbase

To Configure Cassandra Data Store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently, there’s no configuration needed for Cassandra Data Store. The
user can use Cassandra data store directly after installing the feature
from Karaf console.

Additionally separate commands have been implemented to install various
data collectors.

Administering or Managing TSDR Data Stores
------------------------------------------

To Administer HSQLDB Data Store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the TSDR default datastore feature (odl-tsdr-hsqldb-all) is
enabled, the TSDR captured OpenFlow statistics metrics can be accessed
from Karaf Console by executing the command

::

    tsdr:list <metric-category> <starttimestamp> <endtimestamp>

wherein

-  <metric-category> = any one of the following categories
   FlowGroupStats, FlowMeterStats, FlowStats, FlowTableStats, PortStats,
   QueueStats

-  <starttimestamp> = to filter the list of metrics starting this
   timestamp

-  <endtimestamp> = to filter the list of metrics ending this timestamp

-  <starttimestamp> and <endtimestamp> are optional.

-  Maximum 1000 records will be displayed.

To Administer HBase Data Store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Using Karaf Command to retrieve data from HBase Data Store

The user first need to install hbase data store from karaf console:

feature:install odl-tsdr-hbase

The user can retrieve the data from HBase data store using the following
commands from Karaf console:

::

    tsdr:list
    tsdr:list <CategoryName> <StartTime> <EndTime>

Typing tab will get the context prompt of the arguments when typeing the
command in Karaf console.

To Administer Cassandra Data Store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The user first needs to install Cassandra data store from Karaf console:

::

    feature:install odl-tsdr-cassandra

Then the user can retrieve the data from Cassandra data store using the
following commands from Karaf console:

::

    tsdr:list
    tsdr:list <CategoryName> <StartTime> <EndTime>

Typing tab will get the context prompt of the arguments when typeing the
command in Karaf console.

Installing TSDR Data Collectors
-------------------------------

When the user uses HSQLDB data store and installed "odl-tsdr-hsqldb-all"
feature from Karaf console, besides the HSQLDB data store, OpenFlow data
collector is also installed with this command. However, if the user
needs to use other collectors, such as NetFlow Collector, Syslog
Collector, SNMP Collector, and Controller Metrics Collector, the user
needs to install them with separate commands. If the user uses HBase or
Cassandra data store, no collectors will be installed when the data
store is installed. Instead, the user needs to install each collector
separately using feature install command from Karaf console.

The following is the list of supported TSDR data collectors with the
associated feature install commands:

-  OpenFlow Data Collector

   ::

       feature:install odl-tsdr-openflow-statistics-collector

-  SNMP Data Collector

   ::

       feature:install odl-tsdr-snmp-data-collector

-  NetFlow Data Collector

   ::

       feature:install odl-tsdr-netflow-statistics-collector

-  Syslog Data Collector

   ::

       feature:install odl-tsdr-syslog-collector

-  Controller Metrics Collector

   ::

       feature:install odl-tsdr-controller-metrics-collector

In order to use controller metrics collector, the user needs to install
Sigar library.

The following is the instructions for installing Sigar library on
Ubuntu:

-  Install back end library by "sudo apt-get install
   libhyperic-sigar-java"

-  Execute "export
   LD\_LIBRARY\_PATH=/usr/lib/jni/:/usr/lib:/usr/local/lib" to set the
   path of the JNI (you can add this to the ".bashrc" in your home
   directory)

-  Download the file "sigar-1.6.4.jar". It might be also in your ".m2"
   directory under "~/.m2/resources/org/fusesource/sigar/1.6.4"

-  Create the directory "org/fusesource/sigar/1.6.4" under the "system"
   directory in your controller home directory and place the
   "sigar-1.6.4.jar" there

Configuring TSDR Data Collectors
--------------------------------

-  SNMP Data Collector Device Credential Configuration

After installing SNMP Data Collector, a configuration file under etc/
directory of ODL distribution is generated: etc/tsdr.snmp.cfg is
created.

The following is a sample tsdr.snmp.cfg file:

credentials=[192.168.0.2,public],[192.168.0.3,public]

The above credentials indicate that TSDR SNMP Collector is going to
connect to two devices. The IPAddress and Read community string of these
two devices are (192.168.0.2, public), and (192.168.0.3) respectively.

The user can make changes to this configuration file any time during
runtime. The configuration will be picked up by TSDR in the next cycle
of data collection.

Polling interval configuration for SNMP Collector and OpenFlow Stats Collector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The default polling interval of SNMP Collector and OpenFlow Stats
Collector is 30 seconds and 15 seconds respectively. The user can change
the polling interval through restconf APIs at any time. The new polling
interval will be picked up by TSDR in the next collection cycle.

-  Retrieve Polling Interval API for SNMP Collector

   -  URL:
      http://localhost:8181/restconf/config/tsdr-snmp-data-collector:TSDRSnmpDataCollectorConfig

   -  Verb: GET

-  Update Polling Interval API for SNMP Collector

   -  URL:
      http://localhost:8181/restconf/operations/tsdr-snmp-data-collector:setPollingInterval

   -  Verb: POST

   -  Content Type: application/json

   -  Input Payload:

      ::

          {
             "input": {
                 "interval": "15000"
             }
          }

-  Retrieve Polling Interval API for OpenFlowStats Collector

   -  URL:
      http://localhost:8181/restconf/config/tsdr-openflow-statistics-collector:TSDROSCConfig

   -  Verb: GET

-  Update Polling Interval API for OpenFlowStats Collector

   -  URL:
      http://localhost:8181/restconf/operations/tsdr-openflow-statistics-collector:setPollingInterval

   -  Verb: POST

   -  Content Type: application/json

   -  Input Payload:

      ::

          {
             "input": {
                 "interval": "15000"
             }
          }

Querying TSDR from REST APIs
----------------------------

TSDR provides two REST APIs for querying data stored in TSDR data
stores.

-  Query of TSDR Metrics

   -  URL: http://localhost:8181/tsdr/metrics/query

   -  Verb: GET

   -  Parameters:

      -  tsdrkey=[NID=][DC=][MN=][RK=]

         ::

             The TSDRKey format indicates the NodeID(NID), DataCategory(DC), MetricName(MN), and RecordKey(RK) of the monitored objects.
             For example, the following is a valid tsdrkey:
             [NID=openflow:1][DC=FLOWSTATS][MN=PacketCount][RK=Node:openflow:1,Table:0,Flow:3]
             The following is also a valid tsdrkey:
             tsdrkey=[NID=][DC=FLOWSTATS][MN=][RK=]
             In the case when the sections in the tsdrkey is empty, the query will return all the records in the TSDR data store that matches the filled tsdrkey. In the above example, the query will return all the data in FLOWSTATS data category.
             The query will return only the first 1000 records that match the query criteria.

      -  from=<time\_in\_seconds>

      -  until=<time\_in\_seconds>

The following is an example curl command for querying metric data from
TSDR data store:

curl -G -v -H "Accept: application/json" -H "Content-Type:
application/json" "http://localhost:8181/tsdr/metrics/query"
--data-urlencode "tsdrkey=[NID=][DC=FLOWSTATS][MN=][RK=]"
--data-urlencode "from=0" --data-urlencode "until=240000000"\|more

-  Query of TSDR Log type of data

   -  URL:http://localhost:8181/tsdr/logs/query

   -  Verb: GET

   -  Parameters:

      -  tsdrkey=tsdrkey=[NID=][DC=][RK=]

         ::

             The TSDRKey format indicates the NodeID(NID), DataCategory(DC), and RecordKey(RK) of the monitored objects.
             For example, the following is a valid tsdrkey:
             [NID=openflow:1][DC=NETFLOW][RK]
             The query will return only the first 1000 records that match the query criteria.

      -  from=<time\_in\_seconds>

      -  until=<time\_in\_seconds>

The following is an example curl command for querying log type of data
from TSDR data store:

curl -G -v -H "Accept: application/json" -H "Content-Type:
application/json" "http://localhost:8181/tsdr/logs/query"
--data-urlencode "tsdrkey=[NID=][DC=NETFLOW][RK=]" --data-urlencode
"from=0" --data-urlencode "until=240000000"\|more

Grafana integration with TSDR
-----------------------------

TSDR provides northbound integration with Grafana time series data
visualization tool. All the metric type of data stored in TSDR data
store can be visualized using Grafana.

For the detailed instruction about how to install and configure Grafana
to work with TSDR, please refer to the following link:

https://wiki.opendaylight.org/view/Grafana_Integration_with_TSDR_Step-by-Step

Purging Service configuration
-----------------------------

After the data stores are installed from Karaf console, the purging
service will be installed as well. A configuration file called
tsdr.data.purge.cfg will be generated under etc/ directory of ODL
distribution.

The following is the sample default content of the tsdr.data.purge.cfg
file:

host=127.0.0.1 data\_purge\_enabled=true data\_purge\_time=23:59:59
data\_purge\_interval\_in\_minutes=1440 retention\_time\_in\_hours=168

The host indicates the IPAddress of the data store. In the case when the
data store is together with ODL controller, 127.0.0.1 should be the
right value for the host IP. The other attributes are self-explained.
The user can change those attributes at any time. The configuration
change will be picked up right away by TSDR Purging service at runtime.

How to use TSDR to collect, store, and view OpenFlow Interface Statistics
-------------------------------------------------------------------------

Overview
~~~~~~~~

This tutorial describes an example of using TSDR to collect, store, and
view one type of time series data in OpenDaylight environment.

Prerequisites
~~~~~~~~~~~~~

You would need to have the following as prerequisits:

-  One or multiple OpenFlow enabled switches. Alternatively, you can use
   mininet to simulate such a switch.

-  Successfully installed OpenDaylight Controller.

-  Successfully installed HBase Data Store following TSDR HBase Data
   Store Installation Guide.

-  Connect the OpenFlow enabled switch(es) to OpenDaylight Controller.

Target Environment
~~~~~~~~~~~~~~~~~~

HBase data store is only supported in Linux operation system.

Instructions
~~~~~~~~~~~~

-  Start OpenDaylight.

-  Connect OpenFlow enabled switch(es) to the controller.

   -  If using mininet, run the following commands from mininet command
      line:

      -  mn --topo single,3 --controller
         *remote,ip=172.17.252.210,port=6653* --switch
         ovsk,protocols=OpenFlow13

-  Install tsdr hbase feature from Karaf:

   -  feature:install odl-tsdr-hbase

-  Install OpenFlow Statistics Collector from Karaf:

   -  feature:install odl-tsdr-openflow-statistics-collector

-  run the following command from Karaf console:

   -  tsdr:list PORTSTATS

You should be able to see the interface statistics of the switch(es)
from the HBase Data Store. If there are too many rows, you can use
"tsdr:list InterfaceStats\|more" to view it page by page.

By tabbing after "tsdr:list", you will see all the supported data
categories. For example, "tsdr:list FlowStats" will output the Flow
statistics data collected from the switch(es).

Troubleshooting
---------------

Karaf logs
~~~~~~~~~~

All TSDR features and components write logging information including
information messages, warnings, errors and debug messages into
karaf.log.

HBase and Cassandra logs
~~~~~~~~~~~~~~~~~~~~~~~~

For HBase and Cassandra data stores, the database level logs are written
into HBase log and Cassandra logs.

-  HBase log

   -  HBase log is under <HBase-installation-directory>/logs/.

-  Cassandra log

   -  Cassandra log is under {cassandra.logdir}/system.log. The default
      {cassandra.logdir} is /var/log/cassandra/.

TTP CLI Tools User Guide
========================

Overview
--------

Table Type Patterns are a specification developed by the `Open
Networking Foundation <https://www.opennetworking.org/>`__ to enable the
description and negotiation of subsets of the OpenFlow protocol. This is
particularly useful for hardware switches that support OpenFlow as it
enables the to describe what features they do (and thus also what
features they do not) support. More details can be found in the full
specification listed on the `OpenFlow specifications
page <https://www.opennetworking.org/sdn-resources/onf-specifications/openflow>`__.

TTP CLI Tools Architecture
--------------------------

The TTP CLI Tools use the TTP Model and the YANG Tools/RESTCONF codecs
to translate between the Data Transfer Objects (DTOs) and JSON/XML.

Unified Secure Channel
======================

This document describes how to use the Unified Secure Channel (USC)
feature in OpenDaylight. This document contains configuration,
administration, and management sections for the feature.

Overview
--------

In enterprise networks, more and more controller and network management
systems are being deployed remotely, such as in the cloud. Additionally,
enterprise networks are becoming more heterogeneous - branch, IoT,
wireless (including cloud access control). Enterprise customers want a
converged network controller and management system solution. This
feature is intended for device and network administrators looking to use
unified secure channels for their systems.

USC Channel Architecture
------------------------

-  USC Agent

   -  The USC Agent provides proxy and agent functionality on top of all
      standard protocols supported by the device. It initiates call-home
      with the controller, maintains live connections with with the
      controller, acts as a demuxer/muxer for packets with the USC
      header, and authenticates the controller.

-  USC Plugin

   -  The USC Plugin is responsible for communication between the
      controller and the USC agent . It responds to call-home with the
      controller, maintains live connections with the devices, acts as a
      muxer/demuxer for packets with the USC header, and provides
      support for TLS/DTLS.

-  USC Manager

   -  The USC Manager handles configurations, high availability,
      security, monitoring, and clustering support for USC.

-  USC UI

   -  The USC UI is responsible for displaying a graphical user
      interface representing the state of USC in the OpenDaylight DLUX
      UI.

Installing USC Channel
----------------------

To install USC, download OpenDaylight and use the Karaf console to
install the following feature:

odl-usc-channel-ui

Configuring USC Channel
-----------------------

This section gives details about the configuration settings for various
components in USC.

The USC configuration files for the Karaf distribution are located in
distribution/karaf/target/assembly/etc/usc

-  certificates

   -  The certificates folder contains the client key, pem, and rootca
      files as is necessary for security.

-  akka.conf

   -  This file contains configuration related to clustering. Potential
      configuration properties can be found on the akka website at
      http://doc.akka.io

-  usc.properties

   -  This file contains configuration related to USC. Use this file to
      set the location of certificates, define the source of additional
      akka configurations, and assign default settings to the USC
      behavior.

Administering or Managing USC Channel
-------------------------------------

After installing the odl-usc-channel-ui feature from the Karaf console,
users can administer and manage USC channels from the the UI or APIDOCS
explorer.

Go to
`http://${ipaddress}:8181/index.html <http://${ipaddress}:8181/index.html>`__,
sign in, and click on the USC side menu tab. From there, users can view
the state of USC channels.

Go to
`http://${ipaddress}:8181/apidoc/explorer/index.html <http://${ipaddress}:8181/apidoc/explorer/index.html>`__,
sign in, and expand the usc-channel panel. From there, users can execute
various API calls to test their USC deployment such as add-channel,
delete-channel, and view-channel.

Tutorials
---------

Below are tutorials for USC Channel

Viewing USC Channel
~~~~~~~~~~~~~~~~~~~

The purpose of this tutorial is to view USC Channel

Overview
^^^^^^^^

This tutorial walks users through the process of viewing the USC Channel
environment topology including established channels connecting the
controllers and devices in the USC topology.

Prerequisites
^^^^^^^^^^^^^

For this tutorial, we assume that a device running a USC agent is
already installed.

Instructions
^^^^^^^^^^^^

-  Run the OpenDaylight distribution and install odl-usc-channel-ui from
   the Karaf console.

-  Go to
   `http://${ipaddress}:8181/apidoc/explorer/index.html <http://${ipaddress}:8181/apidoc/explorer/index.html>`__

-  Execute add-channel with the following json data:

   -  {"input":{"channel":{"hostname":"127.0.0.1","port":1068,"remote":false}}}

-  Go to
   `http://${ipaddress}:8181/index.html <http://${ipaddress}:8181/index.html>`__

-  Click on the USC side menu tab.

-  The UI should display a table including the added channel from step
   3.

Virtual Tenant Network (VTN)
============================

VTN Overview
------------

OpenDaylight Virtual Tenant Network (VTN) is an application that
provides multi-tenant virtual network on an SDN controller.

Conventionally, huge investment in the network systems and operating
expenses are needed because the network is configured as a silo for each
department and system. So, various network appliances must be installed
for each tenant and those boxes cannot be shared with others. It is a
heavy work to design, implement and operate the entire complex network.

The uniqueness of VTN is a logical abstraction plane. This enables the
complete separation of logical plane from physical plane. Users can
design and deploy any desired network without knowing the physical
network topology or bandwidth restrictions.

VTN allows the users to define the network with a look and feel of
conventional L2/L3 network. Once the network is designed on VTN, it will
automatically be mapped into underlying physical network, and then
configured on the individual switch leveraging SDN control protocol. The
definition of logical plane makes it possible not only to hide the
complexity of the underlying network but also to better manage network
resources. It achieves reducing reconfiguration time of network services
and minimizing network configuration errors.

.. figure:: ./images/vtn/VTN_Overview.jpg
   :alt: VTN Overview

   VTN Overview

It is implemented as two major components

-  `VTN Manager <#_vtn_manager>`__

-  `VTN Coordinator <#_vtn_coordinator>`__

VTN Manager
~~~~~~~~~~~

An OpenDaylight Controller Plugin that interacts with other modules to
implement the components of the VTN model. It also provides a REST
interface to configure VTN components in ODL controller. VTN Manager is
implemented as one plugin to the OpenDaylight controller. This provides
a REST interface to create/update/delete VTN components. The user
command in VTN Coordinator is translated as REST API to VTN Manager by
the ODC Driver component. In addition to the above mentioned role, it
also provides an implementation to the OpenStack L2 Network Functions
API.

Features Overview
^^^^^^^^^^^^^^^^^

-  **odl-vtn-manager** provides VTN Manager’s JAVA API.

-  **odl-vtn-manager-rest** provides VTN Manager’s REST API.

-  **odl-vtn-manager-neutron** provides the integration with Neutron
   interface.

REST API
^^^^^^^^

VTN Manager provides REST API for virtual network functions.

Here is an example of how to create a virtual tenant network.

::

     curl --user "admin":"admin" -H "Accept: application/json" -H \
     "Content-type: application/json" -X POST \
     http://localhost:8282/controller/nb/v2/vtn/default/vtns/Tenant1 \
     -d '{"description": "My First Virtual Tenant Network"}'

You can check the list of all tenants by executing the following
command.

::

     curl --user "admin":"admin" -H "Accept: application/json" -H \
     "Content-type: application/json" -X GET \
     http://localhost:8282/controller/nb/v2/vtn/default/vtns

REST API documentation for VTN Manager, please refer:
https://jenkins.opendaylight.org/releng/view/vtn/job/vtn-merge-master/lastSuccessfulBuild/artifact/manager/northbound/target/site/wsdocs/rest.html

VTN Coordinator
~~~~~~~~~~~~~~~

The VTN Coordinator is an external application that provides a REST
interface for a user to use the VTN Virtualization. It interacts with
VTN Manager plugin to implement the user configuration. It is also
capable of multiple controller orchestration. It realizes Virtual Tenant
Network (VTN) provisioning in OpenDaylight Controllers (ODC). In the
OpenDaylight architecture VTN Coordinator is part of the network
application, orchestration and services layer. VTN Coordinator has been
implemented as an external application to the OpenDaylight controller.
This component is responsible for the VTN virtualization. VTN
Coordinator will use the REST interface exposed by the VTN Manger to
realize the virtual network using the OpenDaylight controller. It uses
OpenDaylight APIs (REST) to construct the virtual network in ODCs. It
provides REST APIs for northbound VTN applications and supports virtual
networks spanning across multiple ODCs by coordinating across ODCs.

For VTN Coordinator REST API, please refer:
https://wiki.opendaylight.org/view/OpenDaylight_Virtual_Tenant_Network_%28VTN%29:VTN_Coordinator:RestApi

Network Virtualization Function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The user first defines a VTN. Then, the user maps the VTN to a physical
network, which enables communication to take place according to the VTN
definition. With the VTN definition, L2 and L3 transfer functions and
flow-based traffic control functions (filtering and redirect) are
possible.

Virtual Network Construction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows the elements which make up the VTN. In the
VTN, a virtual network is constructed using virtual nodes (vBridge,
vRouter) and virtual interfaces and links. It is possible to configure a
network which has L2 and L3 transfer function, by connecting the virtual
intrefaces made on virtual nodes via virtual links.

+--------------------------------------+--------------------------------------+
| vBridge                              | The logical representation of L2     |
|                                      | switch function.                     |
+--------------------------------------+--------------------------------------+
| vRouter                              | The logical representation of router |
|                                      | function.                            |
+--------------------------------------+--------------------------------------+
| vTep                                 | The logical representation of Tunnel |
|                                      | End Point - TEP.                     |
+--------------------------------------+--------------------------------------+
| vTunnel                              | The logical representation of        |
|                                      | Tunnel.                              |
+--------------------------------------+--------------------------------------+
| vBypass                              | The logical representation of        |
|                                      | connectivity between controlled      |
|                                      | networks.                            |
+--------------------------------------+--------------------------------------+
| Virtual interface                    | The representation of end point on   |
|                                      | the virtual node.                    |
+--------------------------------------+--------------------------------------+
| Virtual Linkv(vLink)                 | The logical representation of L1     |
|                                      | connectivity between virtual         |
|                                      | interfaces.                          |
+--------------------------------------+--------------------------------------+

The following figure shows an example of a constructed virtual network.
VRT is defined as the vRouter, BR1 and BR2 are defined as vBridges.
interfaces of the vRouter and vBridges are connected using vLinks.

.. figure:: ./images/vtn/VTN_Construction.jpg
   :alt: VTN Construction

   VTN Construction

Mapping of Physical Network Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Map physical network resources to the constructed virtual network.
Mapping identifies which virtual network each packet transmitted or
received by an OpenFlow switch belongs to, as well as which interface in
the OpenFlow switch transmits or receives that packet. There are two
mapping methods. When a packet is received from the OFS, port mapping is
first searched for the corresponding mapping definition, then VLAN
mapping is searched, and the packet is mapped to the relevant vBridge
according to the first matching mapping.

+--------------------------------------+--------------------------------------+
| Port mapping                         | Maps physical network resources to   |
|                                      | an interface of vBridge using Switch |
|                                      | ID, Port ID and VLAN ID of the       |
|                                      | incoming L2 frame. Untagged frame    |
|                                      | mapping is also supported.           |
+--------------------------------------+--------------------------------------+
| VLAN mapping                         | Maps physical network resources to a |
|                                      | vBridge using VLAN ID of the         |
|                                      | incoming L2 frame.Maps physical      |
|                                      | resources of a particular switch to  |
|                                      | a vBridge using switch ID and VLAN   |
|                                      | ID of the incoming L2 frame.         |
+--------------------------------------+--------------------------------------+
| MAC mapping                          | Maps physical resources to an        |
|                                      | interface of vBridge using MAC       |
|                                      | address of the incoming L2 frame(The |
|                                      | initial contribution does not        |
|                                      | include this method).                |
+--------------------------------------+--------------------------------------+

VTN can learn the terminal information from a terminal that is connected
to a switch which is mapped to VTN. Further, it is possible to refer
that terminal information on the VTN.

-  Learning terminal information VTN learns the information of a
   terminal that belongs to VTN. It will store the MAC address and VLAN
   ID of the terminal in relation to the port of the switch.

-  Aging of terminal information Terminal information, learned by the
   VTN, will be maintained until the packets from terminal keep flowing
   in VTN. If the terminal gets disconnected from the VTN, then the
   aging timer will start clicking and the terminal information will be
   maintained till timeout.

The following figure shows an example of mapping. An interface of BR1 is
mapped to port GBE0/1 of OFS1 using port mapping. Packets received from
GBE0/1 of OFS1 are regarded as those from the corresponding interface of
BR1. BR2 is mapped to VLAN 200 using VLAN mapping. Packets with VLAN tag
200 received from any ports of any OFSs are regarded as those from an
interface of BR2.

.. figure:: ./images/vtn/VTN_Mapping.jpg
   :alt: VTN Mapping

   VTN Mapping

vBridge Functions
~~~~~~~~~~~~~~~~~

The vBridge provides the bridge function that transfers a packet to the
intended virtual port according to the destination MAC address. The
vBridge looks up the MAC address table and transmits the packet to the
corresponding virtual interface when the destination MAC address has
been learned. When the destination MAC address has not been learned, it
transmits the packet to all virtual interfaces other than the receiving
port (flooding). MAC addresses are learned as follows.

-  MAC address learning The vBridge learns the MAC address of the
   connected host. The source MAC address of each received frame is
   mapped to the receiving virtual interface, and this MAC address is
   stored in the MAC address table created on a per-vBridge basis.

-  MAC address aging The MAC address stored in the MAC address table is
   retained as long as the host returns the ARP reply. After the host is
   disconnected, the address is retained until the aging timer times
   out. To have the vBridge learn MAC addresses statically, you can
   register MAC addresses manually.

vRouter Functions
~~~~~~~~~~~~~~~~~

The vRouter transfers IPv4 packets between vBridges. The vRouter
supports routing, ARP learning, and ARP aging functions. The following
outlines the functions.

-  Routing function When an IP address is registered with a virtual
   interface of the vRouter, the default routing information for that
   interface is registered. It is also possible to statically register
   routing information for a virtual interface.

-  ARP learning function The vRouter associates a destination IP
   address, MAC address and a virtual interface, based on an ARP request
   to its host or a reply packet for an ARP request, and maintains this
   information in an ARP table prepared for each routing domain. The
   registered ARP entry is retained until the aging timer, described
   later, times out. The vRouter transmits an ARP request on an
   individual aging timer basis and deletes the associated entry from
   the ARP table if no reply is returned. For static ARP learning, you
   can register ARP entry information manually. \*DHCP relay agent
   function The vRouter also provides the DHCP relay agent function.

Flow Filter Functions
~~~~~~~~~~~~~~~~~~~~~

Flow Filter function is similar to ACL. It is possible to allow or
prohibit communication with only certain kind of packets that meet a
particular condition. Also, it can perform a processing called
Redirection - WayPoint routing, which is different from the existing
ACL. Flow Filter can be applied to any interface of a vNode within VTN,
and it is possible to the control the packets that pass interface. The
match conditions that could be specified in Flow Filter are as follows.
It is also possible to specify a combination of multiple conditions.

-  Source MAC address

-  Destination MAC address

-  MAC ether type

-  VLAN Priority

-  Source IP address

-  Destination IP address

-  DSCP

-  IP Protocol

-  TCP/UDP source port

-  TCP/UDP destination port

-  ICMP type

-  ICMP code

The types of Action that can be applied on packets that match the Flow
Filter conditions are given in the following table. It is possible to
make only those packets, which match a particular condition, to pass
through a particular server by specifying Redirection in Action. E.g.,
path of flow can be changed for each packet sent from a particular
terminal, depending upon the destination IP address. VLAN priority
control and DSCP marking are also supported.

+--------------------------------------+--------------------------------------+
| Pass                                 | Pass particular packets matching the |
|                                      | specified conditions.                |
+--------------------------------------+--------------------------------------+
| Drop                                 | Discards particular packets matching |
|                                      | the specified conditions.            |
+--------------------------------------+--------------------------------------+
| Redirection                          | Redirects the packet to a desired    |
|                                      | virtual interface. Both Transparent  |
|                                      | Redirection (not changing MAC        |
|                                      | address) and Router Redirection      |
|                                      | (changing MAC address) are           |
|                                      | supported.                           |
+--------------------------------------+--------------------------------------+

The following figure shows an example of how the flow filter function
works.

If there is any matching condition specified by flow filter when a
packet being transferred within a virtual network goes through a virtual
interface, the function evaluates the matching condition to see whether
the packet matches it. If the packet matches the condition, the function
applies the matching action specified by flow filter. In the example
shown in the figure, the function evaluates the matching condition at
BR1 and discards the packet if it matches the condition.

.. figure:: ./images/vtn/VTN_Flow_Filter.jpg
   :alt: VTN FlowFilter

   VTN FlowFilter

Multiple SDN Controller Coordination
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With the network abstractions, VTN enables to configure virtual network
across multiple SDN controllers. This provides highly scalable network
system.

VTN can be created on each SDN controller. If users would like to manage
those multiple VTNs with one policy, those VTNs can be integrated to a
single VTN.

As a use case, this feature is deployed to multi data center
environment. Even if those data centers are geographically separated and
controlled with different controllers, a single policy virtual network
can be realized with VTN.

Also, one can easily add a new SDN Controller to an existing VTN or
delete a particular SDN Controller from VTN.

In addition to this, one can define a VTN which covers both OpenFlow
network and Overlay network at the same time.

Flow Filter, which is set on the VTN, will be automatically applied on
the newly added SDN Controller.

Coordination between OpenFlow Network and L2/L3 Network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to configure VTN on an environment where there is mix of
L2/L3 switches as well. L2/L3 switch will be shown on VTN as vBypass.
Flow Filter or policing cannot be configured for a vBypass. However, it
is possible to treat it as a virtual node inside VTN.

Virtual Tenant Network (VTN) API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VTN provides Web APIs. They are implemented by REST architecture and
provide the access to resources within VTN that are identified by URI.
User can perform the operations like GET/PUT/POST/DELETE against the
virtual network resources (e.g. vBridge or vRouter) by sending a message
to VTN through HTTPS communication in XML or JSON format.

.. figure:: ./images/vtn/VTN_API.jpg
   :alt: VTN API

   VTN API

Function Outline
^^^^^^^^^^^^^^^^

VTN provides following operations for various network resources.

+----------------+----------------+----------------+----------------+----------------+
| Resources      | GET            | POST           | PUT            | DELETE         |
+----------------+----------------+----------------+----------------+----------------+
| VTN            | Yes            | Yes            | Yes            | Yes            |
+----------------+----------------+----------------+----------------+----------------+
| vBridge        | Yes            | Yes            | Yes            | Yes            |
+----------------+----------------+----------------+----------------+----------------+
| vRouter        | Yes            | Yes            | Yes            | Yes            |
+----------------+----------------+----------------+----------------+----------------+
| vTep           | Yes            | Yes            | Yes            | Yes            |
+----------------+----------------+----------------+----------------+----------------+
| vTunnel        | Yes            | Yes            | Yes            | Yes            |
+----------------+----------------+----------------+----------------+----------------+
| vBypass        | Yes            | Yes            | Yes            | Yes            |
+----------------+----------------+----------------+----------------+----------------+
| vLink          | Yes            | Yes            | Yes            | Yes            |
+----------------+----------------+----------------+----------------+----------------+
| Interface      | Yes            | Yes            | Yes            | Yes            |
+----------------+----------------+----------------+----------------+----------------+
| Port map       | Yes            | No             | Yes            | Yes            |
+----------------+----------------+----------------+----------------+----------------+
| Vlan map       | Yes            | Yes            | Yes            | Yes            |
+----------------+----------------+----------------+----------------+----------------+
| Flowfilter     | Yes            | Yes            | Yes            | Yes            |
| (ACL/redirect) |                |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| Controller     | Yes            | Yes            | Yes            | Yes            |
| information    |                |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| Physical       | Yes            | No             | No             | No             |
| topology       |                |                |                |                |
| information    |                |                |                |                |
+----------------+----------------+----------------+----------------+----------------+
| Alarm          | Yes            | No             | No             | No             |
| information    |                |                |                |                |
+----------------+----------------+----------------+----------------+----------------+

Example usage
^^^^^^^^^^^^^

The following is an example of the usage to construct a virtual network.

-  Create VTN

::

       curl --user admin:adminpass -X POST -H 'content-type: application/json'  \
      -d '{"vtn":{"vtn_name":"VTN1"}}' http://172.1.0.1:8083/vtn-webapi/vtns.json

-  Create Controller Information

::

       curl --user admin:adminpass -X POST -H 'content-type: application/json'  \
      -d '{"controller": {"controller_id":"CONTROLLER1","ipaddr":"172.1.0.1","type":"odc","username":"admin", \
      "password":"admin","version":"1.0"}}' http://172.1.0.1:8083/vtn-webapi/controllers.json

-  Create vBridge under VTN

::

      curl --user admin:adminpass -X POST -H 'content-type: application/json' \
      -d '{"vbridge":{"vbr_name":"VBR1","controller_id": "CONTROLLER1","domain_id": "(DEFAULT)"}}' \
      http://172.1.0.1:8083/vtn-webapi/vtns/VTN1/vbridges.json

-  Create the interface under vBridge

::

      curl --user admin:adminpass -X POST -H 'content-type: application/json' \
      -d '{"interface":{"if_name":"IF1"}}' http://172.1.0.1:8083/vtn-webapi/vtns/VTN1/vbridges/VBR1/interfaces.json

VTN OpenStack Configuration
---------------------------

This guide describes how to set up OpenStack for integration with
OpenDaylight Controller.

While OpenDaylight Controller provides several ways to integrate with
OpenStack, this guide focus on the way which uses VTN features available
on OpenDaylight controller.In the integration, VTN Manager work as
network service provider for OpenStack.

VTN Manager features, enable OpenStack to work in pure OpenFlow
environment in which all switches in data plane are OpenFlow switch.

Requirements
~~~~~~~~~~~~

To use OpenDaylight as Network Service Provider for OpenStack.

Components
~~~~~~~~~~

-  OpenDaylight Controller.

-  OpenStack Control Node.

-  OpenStack Compute Node.

-  OpenFlow Switch like mininet(Not Mandatory).

The VTN features support multiple OpenStack nodes. You can deploy
multiple OpenStack Compute Nodes. In management plane, OpenDaylight
Controller, OpenStack nodes and OpenFlow switches should communicate
with each other. In data plane, Open vSwitches running in OpenStack
nodes should communicate with each other through a physical or logical
OpenFlow switches. The core OpenFlow switches are not mandatory.
Therefore, you can directly connect to the Open vSwitch’s.

.. figure:: ./images/vtn/vtn_devstack_setup.png
   :alt: LAB Setup

   LAB Setup

    **Note**

    Ubuntu 14.04 was used in both the nodes and Vsphere was used for
    this howto.

Configuration
~~~~~~~~~~~~~

**Server Preparation**

-  Install Ubuntu 14.04 LTS in two servers (OpenStack Control node and
   Compute node respectively)

-  While installing, Ubuntu mandates creation of a User, we created the
   user "stack"(We will use the same user for running devstack) NOTE:
   You can also have multiple Compute nodes. TIP: Please do minimal
   Install to avoid any issues in devstack bringup

**User Settings** - Login to both servers - Disable Ubuntu Firewall

::

    sudo ufw disable

-  Optionally install these packages

   ::

       sudo apt-get install net-tools

-  Edit sudo vim /etc/sudoers and add an entry as follows

   ::

       stack ALL=(ALL) NOPASSWD: ALL

**Network Settings** - Checked the output of ifconfig -a, two interfaces
were listed eth0 and eth1 as indicated in the image above. - We had
connected eth0 interface to the Network where OpenDaylight is reachable.
- eth1 interface in both servers were connected to a different network
to act as data plane for the VM’s created using the OpenStack. -
Manually edited the file : sudo vim /etc/network/interfaces and made
entries as follows

::

     stack@ubuntu-devstack:~/devstack$ cat /etc/network/interfaces
     # This file describes the network interfaces available on your system
     # and how to activate them. For more information, see interfaces(5).
     # The loop-back network interface
     auto lo
     iface lo inet loopback
     # The primary network interface
     auto eth0
     iface eth0 inet static
          address <IP_ADDRESS_TO_REACH_ODL>
          netmask <NET_MASK>
          broadcast <BROADCAST_IP_ADDRESS>
          gateway <GATEWAY_IP_ADDRESS>
    auto eth1
    iface eth1 inet static
         address <IP_ADDRESS_UNIQ>
         netmask <NETMASK>

    **Note**

    Please ensure that the eth0 interface is the default route and it is
    able to reach the ODL\_IP\_ADDRESS NOTE: The entries for eth1 are
    not mandatory, If not set, we may have to manually do "ifup eth1"
    after the stacking is complete to activate the interface

**Finalize** - reboot both nodes after the user and network settings to
have the network settings applied to the network - Login again and check
the output of ifconfig to ensure that both interfaces are listed

OpenDaylight Settings and Execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

vtn.ini
^^^^^^^

-  VTN uses the configuration parameters from *vtn.ini* file for the
   OpenStack integration.

-  These values will be set for the OpenvSwitch, in all the
   participating OpenStack nodes.

-  A configuration file *vtn.ini*'*' needs to be created manually in the
   'configuration* directory.

-  The contents of *vtn.ini* should be as follows:

bridgename=br-int portname=eth1 protocols=OpenFlow13 failmode=secure

-  The values of the configuration parameters must be changed based on
   the user environment.

-  Especially, "portname" should be carefully configured, because if the
   value is wrong, OpenDaylight controller fails to forward packets.

-  Other parameters works fine as is for general use cases.

   -  bridgename

      -  The name of the bridge in Open vSwitch, that will be created by
         OpenDaylight Controller.

      -  It must be "br-int".

   -  portname

      -  The name of the port that will be created in the vbridge in
         Open vSwitch.

      -  This must be the same name of the interface of OpenStack Nodes
         which is used for interconnecting OpenStack Nodes in data
         plane.(in our case:eth1)

      -  By default, if vtn.ini is not created, VTN uses ens33 as
         portname.

   -  protocols

      -  OpenFlow protocol through which OpenFlow Switch and Controller
         communicate.

      -  The values can be OpenFlow13 or OpenFlow10.

   -  failmode

      -  The value can be "standalone" or "secure".

      -  Please use "secure" for general use cases.

Start OpenDaylight
~~~~~~~~~~~~~~~~~~

-  Please install the feature **odl-vtn-manager-neutron** that provides
   the integration with Neutron interface.

feature:install odl-vtn-manager-neutron

    **Tip**

    After running OpenDaylight, please ensure OpenDaylight listens to
    the ports:6633,6653, 6640 and 8080

    **Tip**

    Please allow the ports in firewall for the devstack to be able to
    communicate with OpenDaylight.

    **Note**

    \* 6633/6653 - OpenFlow Ports \* 6640 - Open vSwitch Manager Port \*
    8282 - Port for REST API

Devstack Setup
~~~~~~~~~~~~~~

VTN Devstack Script
^^^^^^^^^^^^^^^^^^^

-  The local.conf is a user-maintained settings file. This allows all
   custom settings for DevStack to be contained in a single file. This
   file is processed strictly in sequence. The following datas are
   needed to be set in the local.conf file:

-  Set the Host\_IP as the detection is unreliable.

-  Set FLOATING\_RANGE to a range not used on the local network, i.e.
   192.168.1.224/27. This configures IP addresses ending in 225-254 to
   be used as floating IPs.

-  Set FLAT\_INTERFACE to the Ethernet interface that connects the host
   to your local network. This is the interface that should be
   configured with the static IP address mentioned above.

-  If the \*\_PASSWORD variables are not set, we will be prompted to
   enter values during the execution of stack.sh.

-  Set ADMIN\_PASSWORD . This password is used for the admin and demo
   accounts set up as OpenStack users. We can login to the OpenStack GUI
   with this credentials only.

-  Set the MYSQL\_PASSWORD. The default here is a random hex string
   which is inconvenient if you need to look at the database directly
   for anything.

-  Set the RABBIT\_PASSWORD. This is used by messaging services used by
   both the nodes.

-  Set the service password. This is used by the OpenStack services
   (Nova, Glance, etc) to authenticate with Keystone.

DevStack Control
''''''''''''''''

local.conf(control)

::

    #IP Details
    HOST_IP=<CONTROL_NODE_MANAGEMENT_IF_IP_ADDRESS>#Please Add The Control Node IP Address in this line
    FLAT_INTERFACE=<FLAT_INTERFACE_NAME>
    SERVICE_HOST=$HOST_IP
    #Instance Details
    MULTI_HOST=1
    #config Details
    RECLONE=yes #Make it "no" after stacking successfully the first time
    VERBOSE=True
    LOG_COLOR=True
    LOGFILE=/opt/stack/logs/stack.sh.log
    SCREEN_LOGDIR=/opt/stack/logs
    #OFFLINE=True #Uncomment this after stacking successfully the first time
    #Passwords
    ADMIN_PASSWORD=labstack
    MYSQL_PASSWORD=supersecret
    RABBIT_PASSWORD=supersecret
    SERVICE_PASSWORD=supersecret
    SERVICE_TOKEN=supersecrettoken
    ENABLE_TENANT_TUNNELS=false
    #Services
    disable_service rabbit
    enable_service qpid
    enable_service quantum
    enable_service n-cpu
    enable_service n-cond
    disable_service n-net
    enable_service q-svc
    enable_service q-dhcp
    enable_service q-meta
    enable_service horizon
    enable_service quantum
    enable_service tempest
    ENABLED_SERVICES+=,n-api,n-crt,n-obj,n-cpu,n-cond,n-sch,n-novnc,n-cauth,n-cauth,nova
    ENABLED_SERVICES+=,cinder,c-api,c-vol,c-sch,c-bak
    #ML2 Details
    Q_PLUGIN=ml2
    Q_ML2_PLUGIN_MECHANISM_DRIVERS=opendaylight
    Q_ML2_TENANT_NETWORK_TYPE=local
    Q_ML2_PLUGIN_TYPE_DRIVERS=local
    disable_service n-net
    enable_service q-svc
    enable_service q-dhcp
    enable_service q-meta
    enable_service neutron
    enable_service odl-compute
    ODL_MGR_IP=<ODL_IP_ADDRESS> #Please Add the ODL IP Address in this line
    OVS_PHYSICAL_BRIDGE=br-int
    Q_OVS_USE_VETH=True
    url=http://<ODL_IP_ADDRESS>:8080/controller/nb/v2/neutron #Please Add the ODL IP Address in this line
    username=admin
    password=admin

DevStack Compute
''''''''''''''''

local.conf(compute)

::

    #IP Details
    HOST_IP=<COMPUTE_NODE_MANAGEMENT_IP_ADDRESS> #Add the Compute node Management IP Address
    SERVICE_HOST=<CONTROLLEr_NODE_MANAGEMENT_IP_ADDRESS> #Add the cotnrol Node Management IP Address here
    #Instance Details
    MULTI_HOST=1
    #config Details
    RECLONE=yes #Make thgis "no" after stacking successfully once
    #OFFLINE=True #Uncomment this line after stacking successfuly first time.
    VERBOSE=True
    LOG_COLOR=True
    LOGFILE=/opt/stack/logs/stack.sh.log
    SCREEN_LOGDIR=/opt/stack/logs
    #Passwords
    ADMIN_PASSWORD=labstack
    MYSQL_PASSWORD=supersecret
    RABBIT_PASSWORD=supersecret
    SERVICE_PASSWORD=supersecret
    SERVICE_TOKEN=supersecrettoken
    #Services
    ENABLED_SERVICES=n-cpu,rabbit,neutron
    #ML2 Details
    Q_PLUGIN=ml2
    Q_ML2_PLUGIN_MECHANISM_DRIVERS=opendaylight
    Q_ML2_TENANT_NETWORK_TYPE=local
    Q_ML2_PLUGIN_TYPE_DRIVERS=local
    enable_service odl-compute
    ODL_MGR_IP=<ODL_IP_ADDRESS> #ADD ODL IP address here
    OVS_PHYSICAL_BRIDGE=br-int
    ENABLE_TENANT_TUNNELS=false
    Q_OVS_USE_VETH=True
    #Details of the Control node for various services
    [[post-config|/etc/neutron/plugins/ml2/ml2_conf.ini]]
    Q_HOST=$SERVICE_HOST
    MYSQL_HOST=$SERVICE_HOST
    RABBIT_HOST=$SERVICE_HOST
    GLANCE_HOSTPORT=$SERVICE_HOST:9292
    KEYSTONE_AUTH_HOST=$SERVICE_HOST
    KEYSTONE_SERVICE_HOST=$SERVICE_HOST
    NOVA_VNC_ENABLED=True
    NOVNCPROXY_URL="http://<CONTROLLER_NODE_IP_ADDRESS>:6080/vnc_auto.html" #Add Controller Node IP address
    VNCSERVER_LISTEN=$HOST_IP
    VNCSERVER_PROXYCLIENT_ADDRESS=$VNCSERVER_LISTEN

Devstack Kilo\_Liberty Control Node
'''''''''''''''''''''''''''''''''''

::

    #IP Details
    HOST_IP=<CONTROL_NODE_MANAGEMENT_IF_IP_ADDRESS> #Please Add The Control Node IP Address in this line
    SERVICE_HOST=$HOST_IP
    LOGFILE=stack.sh.log
    SCREEN_LOGDIR=/opt/stack/data/log
    LOG_COLOR=False
    disable_service n-net
    enable_service q-svc
    enable_service q-agt
    enable_service q-meta
    disable_service q-l3
    enable_service n-cpu
    enable_service q-dhcp
    enable_service n-cauth
    enable_service neutron
    enable_service tempest
    ADMIN_PASSWORD=labstack
    MYSQL_PASSWORD=supersecret
    RABBIT_PASSWORD=supersecret
    SERVICE_PASSWORD=supersecret
    SERVICE_TOKEN=supersecrettoken
    ENABLE_TENANT_TUNNELS=True
    NEUTRON_CREATE_INITIAL_NETWORKS=False
    #enable_plugin networking-odl http://git.openstack.org/openstack/networking-odl stable/kilo # Please uncomment this line if you
    want to use stable/kilo branch
    #enable_plugin networking-odl http://git.openstack.org/openstack/networking-odl stable/liberty # Please uncomment this line if you
    want to use stable/liberty branch
    ODL_MODE=externalodl
    ODL_MGR_IP=<ODL_IP_ADDRESS> # Please Add the ODL IP Address in this line
    ODL_PORT=8080
    ODL_USERNAME=admin
    ODL_PASSWORD=admin
    OVS_PHYSICAL_BRIDGE=br-int
    Q_OVS_USE_VETH=True
    Q_ML2_TENANT_NETWORK_TYPE=local
    VNCSERVER_PROXYCLIENT_ADDRESS=$SERVICE_HOST
    VNCSERVER_LISTEN=0.0.0.0
    MYSQL_HOST=$SERVICE_HOST
    RABBIT_HOST=$SERVICE_HOST
    GLANCE_HOSTPORT=$SERVICE_HOST:9292
    KEYSTONE_AUTH_HOST=$SERVICE_HOST
    KEYSTONE_SERVICE_HOST=$SERVICE_HOST
    [[post-config|/etc/neutron/plugins/ml2/ml2_conf.ini]]
    [agent]
    minimize_polling=True

Devstack Kilo\_Liberty Compute Node
'''''''''''''''''''''''''''''''''''

::

    #IP Details
    HOST_IP=<COMPUTE_NODE_IP_ADDRESS>
    SERVICE_HOST=<CONTROL_NODE_IP_ADDRESS>
    LOGFILE=stack.sh.log
    SCREEN_LOGDIR=/opt/stack/data/log
    LOG_COLOR=False
    RECLONE=yes # Make it "no" after stacking successfully the first time
    #OFFLINE=True # Uncomment this after stacking successfully the first time
    disable_all_services
    enable_service n-cpu
    NOVA_VNC_ENABLED=True
    ADMIN_PASSWORD=labstack
    MYSQL_PASSWORD=supersecret
    RABBIT_PASSWORD=supersecret
    SERVICE_PASSWORD=supersecret
    SERVICE_TOKEN=supersecrettoken
    ENABLE_TENANT_TUNNELS=True
    NEUTRON_CREATE_INITIAL_NETWORKS=False
    #enable_plugin networking-odl http://git.openstack.org/openstack/networking-odl stable/kilo # Please uncomment this line if you
    want to use stable/kilo branch
    #enable_plugin networking-odl http://git.openstack.org/openstack/networking-odl stable/liberty # Please uncomment this line if you
    want to use stable/liberty branch
    ODL_MODE=compute
    ODL_MGR_IP=<ODL_IP_ADDRESS> # Please Add the ODL IP Address in this line
    ODL_PORT=8080
    ODL_USERNAME=admin
    ODL_PASSWORD=admin
    OVS_PHYSICAL_BRIDGE=br-int
    VNCSERVER_PROXYCLIENT_ADDRESS=$HOST_IP
    VNCSERVER_LISTEN=0.0.0.0
    MYSQL_HOST=$SERVICE_HOST
    RABBIT_HOST=$SERVICE_HOST
    GLANCE_HOSTPORT=$SERVICE_HOST:9292
    KEYSTONE_AUTH_HOST=$SERVICE_HOST
    KEYSTONE_SERVICE_HOST=$SERVICE_HOST
    [[post-config|/etc/neutron/plugins/ml2/ml2_conf.ini]]
    [agent]
    minimize_polling=True

    **Note**

    We have to comment OFFLINE=TRUE in local.conf files, this will make
    all the installations to happen automatically. RECLONE=yes only when
    we set up the DevStack environment from scratch.

Get Devstack (All nodes)
^^^^^^^^^^^^^^^^^^^^^^^^

-  Install git application using

   -  sudo apt-get install git

-  Get devstack

   -  git clone https://git.openstack.org/openstack-dev/devstack;

-  Switch to stable/Juno Version branch

   -  cd devstack

   -  git checkout stable/juno

    **Note**

    If you want to use stable/kilo Version branch, Please execute the
    below command in devstack folder

::

    git checkout stable/kilo

    **Note**

    If you want to use stable/liberty Version branch, Please execute the
    below command in devstack folder

::

    git checkout stable/liberty

Stack Control Node
^^^^^^^^^^^^^^^^^^

**local.conf: `DevStack Control <#_devstack_control>`__.**

cd devstack in the controller node

-  Copy the contents of local.conf for juno (devstack control node) from
   `DevStack Control <#_devstack_control>`__ and save it as "local.conf"
   in the "devstack".

-  Copy the contents of local.conf for kilo and liberty (devstack
   control node) from `Devstack Kilo\_Liberty Control
   Node <#_devstack_kilo_liberty_control_node>`__ and save it as
   "local.conf" in the "devstack".

-  Please modify the IP Address values as required.

-  Stack the node

   ::

       ./stack.sh

Verify Control Node stacking
''''''''''''''''''''''''''''

-  stack.sh prints out Horizon is now available at
   `http://<CONTROL\_NODE\_IP\_ADDRESS>:8080/ <http://<CONTROL_NODE_IP_ADDRESS>:8080/>`__

-  Execute the command *sudo ovs-vsctl show* in the control node
   terminal and verify if the bridge *br-int* is created.

Stack Compute Node
^^^^^^^^^^^^^^^^^^

**local.conf: `DevStack Compute <#_devstack_compute>`__.**

cd devstack in the controller node

-  Copy the contents of local.conf for juno (devstack compute node) from
   `DevStack Compute <#_devstack_compute>`__ and save it as "local.conf"
   in the "devstack".

-  Copy the contents of local.conf file for kilo and liberty (devstack
   compute node) from `Devstack Kilo\_Liberty Compute
   Node <#_devstack_kilo_liberty_compute_node>`__ and save it as
   "local.conf" in the "devstack".

-  Please modify the IP Address values as required.

-  Stack the node

   ::

       ./stack.sh

Verify Compute Node Stacking
''''''''''''''''''''''''''''

-  stack.sh prints out This is your host ip:
   <COMPUTE\_NODE\_IP\_ADDRESS>

-  Execute the command *sudo ovs-vsctl show* in the control node
   terminal and verify if the bridge *br-int* is created.

-  The output of the ovs-vsctl show will be similar to the one seen in
   control node.

Additional Verifications
^^^^^^^^^^^^^^^^^^^^^^^^

-  Please visit the OpenDaylight DLUX GUI after stacking all the nodes,
   `http://<ODL\_IP\_ADDRESS>:8181/dlux/index.html <http://<ODL_IP_ADDRESS>:8181/dlux/index.html>`__.
   The switches, topology and the ports that are currently read can be
   validated.

    **Tip**

    If the interconnected between the Open vSwitch is not seen, Please
    bring up the interface for the dataplane manually using the below
    comamnd

::

    ifup <interface_name>

    **Tip**

    Some versions of Open vSwitch, drop packets when there is a
    table-miss, So please add the below flow to all the nodes with Open
    vSwitch version (>=2.1)

::

    ovs-ofctl --protocols=OpenFlow13 add-flow br-int priority=0,actions=output:CONTROLLER

    **Tip**

    Please Accept Promiscuous mode in the networks involving the
    interconnect.

Create VM from Devstack Horizon GUI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Login to
   `http://<CONTROL\_NODE\_IP>:8080/ <http://<CONTROL_NODE_IP>:8080/>`__
   to check the horizon GUI.

.. figure:: ./images/vtn/OpenStackGui.png
   :alt: Horizon GUI

   Horizon GUI

Enter the value for User Name as admin and enter the value for Password
as labstack.

-  We should first ensure both the hypervisors(control node and compute
   node) are mapped under hypervisors by clicking on Hpervisors tab.

.. figure:: ./images/vtn/Hypervisors.png
   :alt: Hypervisors

   Hypervisors

-  Create a new Network from Horizon GUI.

-  Click on Networks Tab.

-  click on the Create Network button.

.. figure:: ./images/vtn/Create_Network.png
   :alt: Create Network

   Create Network

-  A popup screen will appear.

-  Enter network name and click Next button.

.. figure:: ./images/vtn/Creare_Network_Step_1.png
   :alt: Step 1

   Step 1

-  Create a sub network by giving Network Address and click Next button
   .

.. figure:: ./images/vtn/Create_Network_Step_2.png
   :alt: Step 2

   Step 2

-  Specify the additional details for subnetwork (please refer the image
   for your reference).

.. figure:: ./images/vtn/Create_Network_Step_3.png
   :alt: Step 3

   Step 3

-  Click Create button

-  Create VM Instance

-  Navigate to Instances tab in the GUI.

.. figure:: ./images/vtn/Instance_Creation.png
   :alt: Instance Creation

   Instance Creation

-  Click on Launch Instances button.

.. figure:: ./images/vtn/Launch_Instance.png
   :alt: Launch Instance

   Launch Instance

-  Click on Details tab to enter the VM details.For this demo we are
   creating Ten VM’s(instances).

-  In the Networking tab, we must select the network,for this we need to
   drag and drop the Available networks to Selected Networks (i.e.,)
   Drag vtn1 we created from Available networks to Selected Networks and
   click Launch to create the instances.

.. figure:: ./images/vtn/Launch_Instance_network.png
   :alt: Launch Network

   Launch Network

-  Ten VM’s will be created.

.. figure:: ./images/vtn/Load_All_Instances.png
   :alt: Load All Instances

   Load All Instances

-  Click on any VM displayed in the Instances tab and click the Console
   tab.

.. figure:: ./images/vtn/Instance_Console.png
   :alt: Instance Console

   Instance Console

-  Login to the VM console and verify with a ping command.

.. figure:: ./images/vtn/Instance_ping.png
   :alt: Ping

   Ping

Verification of Control and Compute Node after VM creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Every time a new VM is created, more interfaces are added to the
   br-int bridge in Open vSwitch.

-  Use **sudo ovs-vsctl show** to list the number of interfaces added.

-  Please visit the DLUX GUI to list the new nodes in every switch.

Using the DLUX GUI
~~~~~~~~~~~~~~~~~~

For more information see `the chapter on
DLUX <#_using_the_opendaylight_user_interface_dlux>`__ above.

References
^^^^^^^^^^

-  http://devstack.org/guides/multinode-lab.html

-  https://wiki.opendaylight.org/view/File:Vtn_demo_hackfest_2014_march.pdf

VTN Usage Examples
------------------

How to configure L2 Network with Single Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
^^^^^^^^

This example provides the procedure to demonstrate configuration of VTN
Coordinator with L2 network using VTN Virtualization(single controller).
Here is the Example for vBridge Interface Mapping with Single Controller
using mininet. mininet details and set-up can be referred at below URL:
https://wiki.opendaylight.org/view/OpenDaylight_Controller:Installation#Using_Mininet

.. figure:: ./images/vtn/vtn-single-controller-topology-example.png
   :alt: EXAMPLE DEMONSTRATING SINGLE CONTROLLER

   EXAMPLE DEMONSTRATING SINGLE CONTROLLER

Requirements
^^^^^^^^^^^^

-  Configure mininet and create a topology:

::

    mininet@mininet-vm:~$ sudo mn --controller=remote,ip=<controller-ip> --topo tree,2

-  mininet> net

::

     s1 lo:  s1-eth1:h1-eth0 s1-eth2:s2-eth1
     s2 lo:  s2-eth1:s1-eth2 s2-eth2:h2-eth0
     h1 h1-eth0:s1-eth1
     h2 h2-eth0:s2-eth2

Configuration
^^^^^^^^^^^^^

-  Create a Controller

::

    curl --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"controller": {"controller_id": "controllerone", "ipaddr":"10.0.0.2", "type": "odc", "version": "1.0", "auditstatus":"enable"}}' http://127.0.0.1:8083/vtn-webapi/controllers.json

-  Create a VTN

::

    curl --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"vtn" : {"vtn_name":"vtn1","description":"test VTN" }}' http://127.0.0.1:8083/vtn-webapi/vtns.json

-  Create a vBridge in the VTN

::

     curl --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"vbridge" : {"vbr_name":"vBridge1","controller_id":"controllerone","domain_id":"(DEFAULT)" }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges.json

-  Create two Interfaces into the vBridge

::

    curl --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"interface": {"if_name": "if1","description": "if_desc1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/interfaces.json

::

    curl --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"interface": {"if_name": "if2","description": "if_desc2"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/interfaces.json

-  Get the list of logical ports configured

::

    Curl --user admin:adminpass -H 'content-type: application/json' -X GET http://127.0.0.1:8083/vtn-webapi/controllers/controllerone/domains/\(DEFAULT\)/logical_ports.json

-  Configure two mappings on the interfaces

::

    curl --user admin:adminpass -H 'content-type: application/json' -X PUT -d '{"portmap":{"logical_port_id": "PP-OF:00:00:00:00:00:00:00:03-s3-eth1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/interfaces/if1/portmap.json
    curl --user admin:adminpass -H 'content-type: application/json' -X PUT -d '{"portmap":{"logical_port_id": "PP-OF:00:00:00:00:00:00:00:02-s2-eth1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/interfaces/if2/portmap.json

Verification
^^^^^^^^^^^^

Please verify whether the Host1 and Host3 are pinging. \* Send packets
from Host1 to Host3

::

    |mininet> h1 ping h3

How to configure L2 Network with Multiple Controllers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  This example provides the procedure to demonstrate configuration of
   VTN Coordinator with L2 network using VTN Virtualization Here is the
   Example for vBridge Interface Mapping with Multi-controller using
   mininet.

.. figure:: ./images/vtn/MutiController_Example_diagram.png
   :alt: EXAMPLE DEMONSTRATING MULTIPLE CONTROLLERS

   EXAMPLE DEMONSTRATING MULTIPLE CONTROLLERS

Requirements
^^^^^^^^^^^^

-  Configure multiple controllers using the mininet script given below:
   https://wiki.opendaylight.org/view/OpenDaylight_Virtual_Tenant_Network_%28VTN%29:Scripts:Mininet#Network_with_Multiple_Paths_for_delivering_packets

Configuration
^^^^^^^^^^^^^

-  Create a VTN

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"vtn" : {"vtn_name":"vtn3"}}' http://127.0.0.1:8083/vtn-webapi/vtns.json

-  Create two Controllers

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"controller": {"controller_id": "odc1", "ipaddr":"10.100.9.52", "type": "odc", "version": "1.0", "auditstatus":"enable"}}' http://127.0.0.1:8083/vtn-webapi/controllers.json

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"controller": {"controller_id": "odc2", "ipaddr":"10.100.9.61", "type": "odc", "version": "1.0", "auditstatus":"enable"}}' http://127.0.0.1:8083/vtn-webapi/controllers.json

-  Create two vBridges in the VTN like, vBridge1 in Controller1 and
   vBridge2 in Controller2

::

     curl --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"vbridge" : {"vbr_name":"vbr1","controller_id":"odc1","domain_id":"(DEFAULT)" }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn3/vbridges.json

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"vbridge" : {"vbr_name":"vbr2","controller_id":"odc2","domain_id":"(DEFAULT)" }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn3/vbridges.json

-  Create vBridge Interfaces

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"interface": {"if_name": "if1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn3/vbridges/vbr1/interfaces.json

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"interface": {"if_name": "if2"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn3/vbridges/vbr1/interfaces.json

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"interface": {"if_name": "if1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn3/vbridges/vbr2/interfaces.json

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"interface": {"if_name": "if2"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn3/vbridges/vbr2/interfaces.json

-  Get the list of logical ports configured

::

    curl --user admin:adminpass -H 'content-type: application/json' -X GET http://127.0.0.1:8083/vtn-webapi/controllers/odc1/domains/\(DEFAULT\)/logical_ports/detail.json

-  Create boundary and vLink

::

    curl --user admin:adminpass -H 'content-type: application/json'   -X POST -d '{"boundary": {"boundary_id": "b1", "link": {"controller1_id": "odc1", "domain1_id": "(DEFAULT)", "logical_port1_id": "PP-OF:00:00:00:00:00:00:00:01-s1-eth3", "controller2_id": "odc2", "domain2_id": "(DEFAULT)", "logical_port2_id": "PP-OF:00:00:00:00:00:00:00:04-s4-eth3"}}}' http://127.0.0.1:8083/vtn-webapi/boundaries.json

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"vlink": {"vlk_name": "vlink1" , "vnode1_name": "vbr1", "if1_name":"if2", "vnode2_name": "vbr2", "if2_name": "if2", "boundary_map": {"boundary_id":"b1","vlan_id": "50"}}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn3/vlinks.json

-  Configure port-map on the interfaces

::

    curl --user admin:adminpass -H 'content-type: application/json' -X PUT -d '{"portmap":{"logical_port_id": "PP-OF:00:00:00:00:00:00:00:02-s2-eth2"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn3/vbridges/vbr1/interfaces/if1/portmap.json

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X PUT -d '{"portmap":{"logical_port_id": "PP-OF:00:00:00:00:00:00:00:05-s5-eth2"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn3/vbridges/vbr2/interfaces/if1/portmap.json

Verification
^^^^^^^^^^^^

Please verify whether Host h2 and Host h6 are pinging. \* Send packets
from h2 to h6

::

    mininet> h2 ping h6

How To Test Vlan-Map In Mininet Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
^^^^^^^^

This example explains how to test vlan-map in a multi host scenario.

.. figure:: ./images/vtn/vlanmap_using_mininet.png
   :alt: Example that demonstrates vlanmap testing in Mininet
   Environment

   Example that demonstrates vlanmap testing in Mininet Environment

Requirements
^^^^^^^^^^^^

-  Save the mininet script given below as vlan\_vtn\_test.py and run the
   mininet script in the mininet environment where Mininet is installed.

Mininet Script
^^^^^^^^^^^^^^

https://wiki.opendaylight.org/view/OpenDaylight_Virtual_Tenant_Network_(VTN):Scripts:Mininet#Network_with_hosts_in_different_vlan

-  Run the mininet script

::

    sudo mn --controller=remote,ip=192.168.64.13 --custom vlan_vtn_test.py --topo mytopo

Configuration
^^^^^^^^^^^^^

Please follow the below steps to test a vlan map using mininet: \*
Create a controller

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"controller": {"controller_id": "controllerone", "ipaddr":"10.0.0.2", "type": "odc", "version": "1.0", "auditstatus":"enable"}}' http://127.0.0.1:8083/vtn-webapi/controllers

-  Create a VTN

::

    curl -X POST -H 'content-type: application/json' -H 'username: admin' -H 'password: adminpass' -d '{"vtn" : {"vtn_name":"vtn1","description":"test VTN" }}' http://127.0.0.1:8083/vtn-webapi/vtns.json

-  Create a vBridge(vBridge1)

::

    curl -X POST -H 'content-type: application/json' -H 'username: admin' -H 'password: adminpass' -d '{"vbridge" : {"vbr_name":"vBridge1","controller_id":"controllerone","domain_id":"(DEFAULT)" }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges.json

-  Create a vlan map with vlanid 200 for vBridge vBridge1

::

    curl -X POST -H 'content-type: application/json' -H 'username: admin' -H 'password: adminpass' -d '{"vlanmap" : {"vlan_id": 200 }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/vlanmaps.json

-  Create a vBridge (vBridge2)

::

    curl -X POST -H 'content-type: application/json' -H 'username: admin' -H 'password: adminpass' -d '{"vbridge" : {"vbr_name":"vBridge2","controller_id":"controllerone","domain_id":"(DEFAULT)" }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges.json

-  Create a vlan map with vlanid 300 for vBridge vBridge2

::

    curl -X POST -H 'content-type: application/json' -H 'username: admin' -H 'password: adminpass' -d '{"vlanmap" : {"vlan_id": 300 }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge2/vlanmaps.json

Verification
^^^^^^^^^^^^

Ping all in mininet environment to view the host reachability.

::

    mininet> pingall
    Ping: testing ping reachability
    h1 -> X h3 X h5 X
    h2 -> X X h4 X h6
    h3 -> h1 X X h5 X
    h4 -> X h2 X X h6
    h5 -> h1 X h3 X X
    h6 -> X h2 X h4 X

How To View Specific VTN Station Information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates on how to view a specific VTN Station
information.

.. figure:: ./images/vtn/vtn_stations.png
   :alt: EXAMPLE DEMONSTRATING VTN STATIONS

   EXAMPLE DEMONSTRATING VTN STATIONS

Requirement
^^^^^^^^^^^

-  Configure mininet and create a topology:

::

     $ sudo mn --custom /home/mininet/mininet/custom/topo-2sw-2host.py --controller=remote,ip=10.100.9.61 --topo mytopo
    mininet> net

     s1 lo:  s1-eth1:h1-eth0 s1-eth2:s2-eth1
     s2 lo:  s2-eth1:s1-eth2 s2-eth2:h2-eth0
     h1 h1-eth0:s1-eth1
     h2 h2-eth0:s2-eth2

-  Generate traffic by pinging between hosts h1 and h2 after configuring
   the portmaps respectively

::

     mininet> h1 ping h2
     PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
     64 bytes from 10.0.0.2: icmp_req=1 ttl=64 time=16.7 ms
     64 bytes from 10.0.0.2: icmp_req=2 ttl=64 time=13.2 ms

Configuration
^^^^^^^^^^^^^

**Create Controller.**

::

    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"controller": {"controller_id": "controllerone", "ipaddr":"10.100.9.61", "type": "odc", "version": "1.0", "auditstatus":"enable"}}' http://127.0.0.1:8083/vtn-webapi/controllers.json

**Create a VTN.**

::

    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"vtn" : {"vtn_name":"vtn1","description":"test VTN" }}' http://127.0.0.1:8083/vtn-webapi/vtns.json

**Create a vBridge in the VTN.**

::

    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"vbridge" : {"vbr_name":"vBridge1","controller_id":"controllerone","domain_id":"(DEFAULT)" }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges.json

**Create two Interfaces into the vBridge.**

::

    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"interface": {"if_name": "if1","description": "if_desc1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/interfaces.json
    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"interface": {"if_name": "if2","description": "if_desc2"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/interfaces.json

**Configure two mappings on the interfaces.**

::

    curl -v --user admin:adminpass -H 'content-type: application/json' -X PUT -d '{"portmap":{"logical_port_id": "PP-OF:00:00:00:00:00:00:00:01-s1-eth1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/interfaces/if1/portmap.json
    curl -v --user admin:adminpass -H 'content-type: application/json' -X PUT -d '{"portmap":{"logical_port_id": "PP-OF:00:00:00:00:00:00:00:02-s2-eth2"}}' http://17.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/interfaces/if2/portmap.json

**Get the VTN stations information.**

::

    curl -v -X GET -H 'content-type: application/json' -H 'username: admin' -H 'password: adminpass' "http://127.0.0.1:8083/vtn-webapi/vtnstations?controller_id=controllerone&vtn_name=vtn1"

Verification
^^^^^^^^^^^^

::

    curl -v -X GET -H 'content-type: application/json' -H 'username: admin' -H 'password: adminpass' "http://127.0.0.1:8083/vtn-webapi/vtnstations?controller_id=controllerone&vtn_name=vtn1"
    {
       "vtnstations": [
           {
               "domain_id": "(DEFAULT)",
               "interface": {},
               "ipaddrs": [
                   "10.0.0.2"
               ],
               "macaddr": "b2c3.06b8.2dac",
               "no_vlan_id": "true",
               "port_name": "s2-eth2",
               "station_id": "178195618445172",
               "switch_id": "00:00:00:00:00:00:00:02",
               "vnode_name": "vBridge1",
               "vnode_type": "vbridge",
               "vtn_name": "vtn1"
           },
           {
               "domain_id": "(DEFAULT)",
               "interface": {},
               "ipaddrs": [
                   "10.0.0.1"
               ],
               "macaddr": "ce82.1b08.90cf",
               "no_vlan_id": "true",
               "port_name": "s1-eth1",
               "station_id": "206130278144207",
               "switch_id": "00:00:00:00:00:00:00:01",
               "vnode_name": "vBridge1",
               "vnode_type": "vbridge",
               "vtn_name": "vtn1"
           }
       ]
    }

How To View Dataflows in VTN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates on how to view a specific VTN Dataflow
information.

Configuration
^^^^^^^^^^^^^

The same Configuration as Vlan Mapping
Example(\ https://wiki.opendaylight.org/view/OpenDaylight_Virtual_Tenant_Network_(VTN):VTN_Coordinator:RestApi:How_to_test_vlan-map_in_Mininet_environment)

Verification
^^^^^^^^^^^^

Get the VTN Dataflows information

::

    curl -v -X GET -H 'content-type: application/json' --user 'admin:adminpass' "http://127.0.0.1:8083/vtn-webapi/dataflows?controller_id=controllerone&srcmacaddr=924c.e4a3.a743&vlan_id=300&switch_id=00:00:00:00:00:00:00:02&port_name=s2-eth1"

::

    {
       "dataflows": [
           {
               "controller_dataflows": [
                   {
                       "controller_id": "controllerone",
                       "controller_type": "odc",
                       "egress_domain_id": "(DEFAULT)",
                       "egress_port_name": "s3-eth3",
                       "egress_station_id": "3",
                       "egress_switch_id": "00:00:00:00:00:00:00:03",
                       "flow_id": "29",
                       "ingress_domain_id": "(DEFAULT)",
                       "ingress_port_name": "s2-eth2",
                       "ingress_station_id": "2",
                       "ingress_switch_id": "00:00:00:00:00:00:00:02",
                       "match": {
                           "macdstaddr": [
                               "4298.0959.0e0b"
                           ],
                           "macsrcaddr": [
                               "924c.e4a3.a743"
                           ],
                           "vlan_id": [
                               "300"
                           ]
                       },
                       "pathinfos": [
                           {
                               "in_port_name": "s2-eth2",
                               "out_port_name": "s2-eth1",
                               "switch_id": "00:00:00:00:00:00:00:02"
                           },
                           {
                               "in_port_name": "s1-eth2",
                               "out_port_name": "s1-eth3",
                               "switch_id": "00:00:00:00:00:00:00:01"
                           },
                           {
                               "in_port_name": "s3-eth1",
                               "out_port_name": "s3-eth3",
                               "switch_id": "00:00:00:00:00:00:00:03"
                           }
                       ]
                   }
               ],
               "reason": "success"
           }
       ]
    }

How To Configure Flow Filters Using VTN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
^^^^^^^^

The flow-filter function discards, permits, or redirects packets of the
traffic within a VTN, according to specified flow conditions The table
below lists the actions to be applied when a packet matches the
condition:

+--------------------------------------+--------------------------------------+
| Action                               | Function                             |
+--------------------------------------+--------------------------------------+
| Pass                                 | Permits the packet to pass. As       |
|                                      | options, packet transfer priority    |
|                                      | (set priority) and DSCP change (se t |
|                                      | ip-dscp) is specified.               |
+--------------------------------------+--------------------------------------+
| Drop                                 | Discards the packet.                 |
+--------------------------------------+--------------------------------------+
| Redirect                             | Redirects the packet to a desired    |
|                                      | virtual interface. As an option, it  |
|                                      | is possible to change the MAC        |
|                                      | address when the packet is           |
|                                      | transferred.                         |
+--------------------------------------+--------------------------------------+

.. figure:: ./images/vtn/flow_filter_example.png
   :alt: Flow Filter

   Flow Filter

Following steps explain flow-filter function:

-  When a packet is transferred to an interface within a virtual
   network, the flow-filter function evaluates whether the transferred
   packet matches the condition specified in the flow-list.

-  If the packet matches the condition, the flow-filter applies the
   flow-list matching action specified in the flow-filter.

Requirements
^^^^^^^^^^^^

To apply the packet filter, configure the following:

-  Create a flow-list and flow-listentry.

-  Specify where to apply the flow-filter, for example VTN, vBridge, or
   interface of vBridge.

Configure mininet and create a topology:

::

    $  mininet@mininet-vm:~$ sudo mn --controller=remote,ip=<controller-ip> --topo tree

Please generate the following topology

::

    $  mininet@mininet-vm:~$ sudo mn --controller=remote,ip=<controller-ip> --topo tree,2
    mininet> net
    c0
    s1 lo:  s1-eth1:s2-eth3 s1-eth2:s3-eth3
    s2 lo:  s2-eth1:h1-eth0 s2-eth2:h2-eth0 s2-eth3:s1-eth1
    s3 lo:  s3-eth1:h3-eth0 s3-eth2:h4-eth0 s3-eth3:s1-eth2
    h1 h1-eth0:s2-eth1
    h2 h2-eth0:s2-eth2
    h3 h3-eth0:s3-eth1
    h4 h4-eth0:s3-eth2

Configuration
^^^^^^^^^^^^^

-  .Create a controller

::

    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"controller": {"controller_id": "controller1", "ipaddr":"10.100.9.61", "type": "odc", "version": "1.0", "auditstatus":"enable"}}' http://127.0.0.1:8083/vtn-webapi/controllers

-  Create a VTN

::

    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"vtn" : {"vtn_name":"vtn_one","description":"test VTN" }}' http://127.0.0.1:8083/vtn-webapi/vtns.json

-  Create two vBridges

::

    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"vbridge" : {"vbr_name":"vbr_one^C"controller_id":"controller1","domain_id":"(DEFAULT)" }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn_one/vbridges.json
    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"vbridge" :
    {"vbr_name":"vbr_two","controller_id":"controller1","domain_id":"(DEFAULT)" }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn_one/vbridges.json

-  Create vBridge interfaces

::

    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"interface": {"if_name": "if1","description": "if_desc1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn_one/vbridges/vbr_two/interfaces.json
    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"interface": {"if_name": "if1","description": "if_desc1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn_one/vbridges/vbr_two/interfaces.json

-  Configure two mappings on the interfaces

::

    curl -v --user admin:adminpass -H 'content-type: application/json' -X PUT -d '{"portmap":{"logical_port_id": "PP-OF:00:00:00:00:00:00:00:03-s3-eth1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn_one/vbridges/vbr_two/interfaces/if1/portmap.json
    curl -v --user admin:adminpass -H 'content-type: application/json' -X PUT -d '{"portmap":{"logical_port_id": "PP-OF:00:00:00:00:00:00:00:02-s2-eth1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn_one/vbridges/vbr_two/interfaces/if2/portmap.json

-  Create Flowlist

::

    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"flowlist": {"fl_name": "flowlist1", "ip_version":"IP"}}' http://127.0.0.1:8083/vtn-webapi/flowlists.json

-  Create Flowlistentry

::

    curl -v --user admin:adminpass -H 'content-type: application/json' -X POST -d '{"flowlistentry": {"seqnum": "233","macethertype": "0x8000","ipdstaddr": "10.0.0.3","ipdstaddrprefix": "2","ipsrcaddr": "10.0.0.2","ipsrcaddrprefix": "2","ipproto": "17","ipdscp": "55","icmptypenum":"232","icmpcodenum": "232"}}' http://127.0.0.1:8083/vtn-webapi/flowlists/flowlist1/flowlistentries.json

-  Create vBridge Interface Flowfilter

::

    curl -v --user admin:adminpass -X POST -H 'content-type: application/json' -d '{"flowfilter" : {"ff_type": "in"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn_one/vbridges/vbr_two/interfaces/if1/flowfilters.json

Flow filter demonstration with DROP action-type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    curl -v --user admin:adminpass -X POST -H 'content-type: application/json' -d '{"flowfilterentry": {"seqnum": "233", "fl_name": "flowlist1", "action_type":"drop", "priority":"3", "dscp":"55" }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn_one/vbridges/vbr_two/interfaces/if1/flowfilters/in/flowfilterentries.json

Verification
^^^^^^^^^^^^

As we have applied the action type "drop" , ping should fail.

::

    mininet> h1 ping h3
    PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
    From 10.0.0.1 icmp_seq=1 Destination Host Unreachable
    From 10.0.0.1 icmp_seq=2 Destination Host Unreachable

In controller you can see the DROP action type information as below,
here action as DROP. osgi> readflows 0000000000000003

::

    [FlowOnNode[flow =Flow[match = Match [fields={DL_VLAN=DL_VLAN(0), IN_PORT=IN_PORT(OF|1@OF|00:00:00:00:00:00:00:03), DL_DST=DL_DST(4e:08:1d:a6:05:08), DL_SRC=DL_SRC(be:15:00:a4:96:13)}, matches=15], actions = [DROP], priority = 10, id = 0, idleTimeout = 0, hardTimeout = 300], tableId = 0, sec = 18, nsec = 475000000, pkt = 20, byte = 1232], FlowOnNode[flow =Flow[match = Match [fields={DL_VLAN=DL_VLAN(0), IN_PORT=IN_PORT(OF|3@OF|00:00:00:00:00:00:00:03), DL_DST=DL_DST(be:15:00:a4:96:13), DL_SRC=DL_SRC(4e:08:1d:a6:05:08)}, matches=15], actions = [OUTPUT[OF|1@OF|00:00:00:00:00:00:00:03]], priority = 10, id = 0, idleTimeout = 0, hardTimeout = 0], tableId = 0, sec = 18, nsec = 489000000, pkt = 10, byte = 812]]

Flow filter demonstration with PASS action-type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    curl -v --user admin:adminpass -X PUT -H 'content-type: application/json' -d '{"flowfilterentry": {"seqnum": "233", "fl_name": "flowlist1", "action_type":"pass", "priority":"3", "dscp":"55" }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn_one/vbridges/vbr_two/interfaces/if1/flowfilters/in/flowfilterentries/233.json

Verification
^^^^^^^^^^^^

::

    mininet> h1 ping h3
    PING 10.0.0.3 (10.0.0.3) 56(84) bytes of data.
    64 bytes from 10.0.0.3: icmp_req=1 ttl=64 time=0.984 ms
    64 bytes from 10.0.0.3: icmp_req=2 ttl=64 time=0.110 ms
    64 bytes from 10.0.0.3: icmp_req=3 ttl=64 time=0.098 ms

In controller you can see the PASS action type information by executing
the following command:

::

     osgi> readflows 0000000000000003

How To Use VTN To Make Packets Take Different Paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates on how to create a specific VTN Path Map
information.

.. figure:: ./images/vtn/Pathmap.png
   :alt: PathMap

   PathMap

Requirement
^^^^^^^^^^^

-  Save the mininet script given below as pathmap\_test.py and run the
   mininet script in the mininet environment where Mininet is installed.

-  Create topology using the below mininet script:

::

    from mininet.topo import Topo
      class MyTopo( Topo ):
        "Simple topology example."
        def __init__( self ):
            "Create custom topo."
            # Initialize topology
            Topo.__init__( self )
            # Add hosts and switches
            leftHost = self.addHost( 'h1' )
            rightHost = self.addHost( 'h2' )
            leftSwitch = self.addSwitch( 's1' )
            middleSwitch = self.addSwitch( 's2' )
            middleSwitch2 = self.addSwitch( 's4' )
            rightSwitch = self.addSwitch( 's3' )
            # Add links
            self.addLink( leftHost, leftSwitch )
            self.addLink( leftSwitch, middleSwitch )
            self.addLink( leftSwitch, middleSwitch2 )
            self.addLink( middleSwitch, rightSwitch )
            self.addLink( middleSwitch2, rightSwitch )
            self.addLink( rightSwitch, rightHost )
     topos = { 'mytopo': ( lambda: MyTopo() ) }

::

     mininet> net
     c0
     s1 lo:  s1-eth1:h1-eth0 s1-eth2:s2-eth1 s1-eth3:s4-eth1
     s2 lo:  s2-eth1:s1-eth2 s2-eth2:s3-eth1
     s3 lo:  s3-eth1:s2-eth2 s3-eth2:s4-eth2 s3-eth3:h2-eth0
     s4 lo:  s4-eth1:s1-eth3 s4-eth2:s3-eth2
     h1 h1-eth0:s1-eth1
     h2 h2-eth0:s3-eth3

-  Generate traffic by pinging between hosts h1 and h2 before creating
   the portmaps respectively

::

      mininet> h1 ping h2
      PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
      From 10.0.0.1 icmp_seq=1 Destination Host Unreachable
      From 10.0.0.1 icmp_seq=2 Destination Host Unreachable
      From 10.0.0.1 icmp_seq=3 Destination Host Unreachable
      From 10.0.0.1 icmp_seq=4 Destination Host Unreachable

Configuration
^^^^^^^^^^^^^

-  Create Controller

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"controller": {"controller_id": "odc", "ipaddr":"10.100.9.42", "type": "odc", "version": "1.0", "auditstatus":"enable"}}' http://127.0.0.1:8083/vtn-webapi/controllers.json

-  Create a VTN

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"vtn" : {"vtn_name":"vtn1","description":"test VTN" }}' http://127.0.0.1:8083/vtn-webapi/vtns.json

-  Create a vBridge in the VTN

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"vbridge" : {"vbr_name":"vBridge1","controller_id":"odc","domain_id":"(DEFAULT)" }}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges.json

-  Create two Interfaces into the vBridge

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"interface": {"if_name": "if1","description": "if_desc1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/interfaces.json
    curl --user admin:adminpass -H 'content-type: application/json'  -X POST -d '{"interface": {"if_name": "if2","description": "if_desc2"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/interfaces.json

-  Configure two mappings on the interfaces

::

    curl --user admin:adminpass -H 'content-type: application/json'  -X PUT -d '{"portmap":{"logical_port_id": "PP-OF:00:00:00:00:00:00:00:01-s1-eth1"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/interfaces/if1/portmap.json
    curl --user admin:adminpass -H 'content-type: application/json'  -X PUT -d '{"portmap":{"logical_port_id": "PP-OF:00:00:00:00:00:00:00:03-s3-eth3"}}' http://127.0.0.1:8083/vtn-webapi/vtns/vtn1/vbridges/vBridge1/interfaces/if2/portmap.json

-  Generate traffic by pinging between hosts h1 and h2 after creating
   the portmaps respectively

::

      mininet> h1 ping h2
      PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
      64 bytes from 10.0.0.2: icmp_req=1 ttl=64 time=36.4 ms
      64 bytes from 10.0.0.2: icmp_req=2 ttl=64 time=0.880 ms
      64 bytes from 10.0.0.2: icmp_req=3 ttl=64 time=0.073 ms
      64 bytes from 10.0.0.2: icmp_req=4 ttl=64 time=0.081 ms

-  Get the VTN Dataflows information

::

    curl -X GET -H 'content-type: application/json' --user 'admin:adminpass' "http://127.0.0.1:8083/vtn-webapi/dataflows?&switch_id=00:00:00:00:00:00:00:01&port_name=s1-eth1&controller_id=odc&srcmacaddr=de3d.7dec.e4d2&no_vlan_id=true"

-  Create a Flowcondition in the VTN

::

    curl --user admin:admin -H 'content-type: application/json' -X PUT -d '{"name": "flowcond_1","match": [{"index": 1,"ethernet": {"src": "ca:9e:58:0c:1e:f0","dst": "ba:bd:0f:e3:a8:c8","type": 2048},"inetMatch": {"inet4": {"src": "10.0.0.1","dst": "10.0.0.2","protocol": 1}}}]}' http://10.100.9.42:8282/controller/nb/v2/vtn/default/flowconditions/flowcond_1

-  Create a Pathmap in the VTN

::

    curl --user admin:admin -H 'content-type: application/json' -X PUT -d '{"index": 10, "condition":"flowcond_1", "policy":1, "idleTimeout": 300, "hardTimeout": 0}' http://10.100.9.42:8282/controller/nb/v2/vtn/default/pathmaps/1

-  Get the Path policy information

::

    curl --user admin:admin -H 'content-type: application/json' -X GET -d '{"id": 1,"default": 100000,"cost": [{"location": {"node": {"type": "OF","id": "00:00:00:00:00:00:00:01"},"port": {"type": "OF","id": "3","name": "s1-eth3"}},"cost": 1000},{"location": {"node": {"type": "OF","id": "00:00:00:00:00:00:00:04"},"port": {"type": "OF","id": "2","name": "s4-eth2"}},"cost": 1000},{"location": {"node": {"type": "OF", "id": "00:00:00:00:00:00:00:03"},"port": {"type": "OF","id": "3","name": "s3-eth3"}},"cost": 100000}]}' http://10.100.9.42:8282/controller/nb/v2/vtn/default/pathpolicies/1

Verification
^^^^^^^^^^^^

-  Before applying Path policy information in the VTN

::

    {
            "pathinfos": [
                {
                  "in_port_name": "s1-eth1",
                  "out_port_name": "s1-eth2",
                  "switch_id": "00:00:00:00:00:00:00:01"
                },
                {
                  "in_port_name": "s2-eth1",
                  "out_port_name": "s2-eth2",
                  "switch_id": "00:00:00:00:00:00:00:02"
                },
                {
                   "in_port_name": "s3-eth1",
                   "out_port_name": "s3-eth3",
                   "switch_id": "00:00:00:00:00:00:00:03"
                }
                         ]
    }

-  After applying Path policy information in the VTN

::

    {
        "pathinfos": [
                {
                  "in_port_name": "s1-eth1",
                  "out_port_name": "s1-eth3",
                  "switch_id": "00:00:00:00:00:00:00:01"
                },
                {
                  "in_port_name": "s4-eth1",
                  "out_port_name": "s4-eth2",
                  "switch_id": "00:00:00:00:00:00:00:04"
                },
                {
                   "in_port_name": "s3-eth2",
                   "out_port_name": "s3-eth3",
                   "switch_id": "00:00:00:00:00:00:00:03"
                }
                         ]
    }

VTN Coordinator(Troubleshooting HowTo)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview
^^^^^^^^

This page demonstrates Installation troubleshooting steps of VTN
Coordinator. OpenDaylight VTN provides multi-tenant virtual network
functions on OpenDaylight controllers. OpenDaylight VTN consists of two
parts:

-  VTN Coordinator.

-  VTN Manager.

VTN Coordinator orchestrates multiple VTN Managers running in
OpenDaylight Controllers, and provides VTN Applications with VTN API.
VTN Manager is OSGi bundles running in OpenDaylight Controller. Current
VTN Manager supports only OpenFlow switches. It handles PACKET\_IN
messages, sends PACKET\_OUT messages, manages host information, and
installs flow entries into OpenFlow switches to provide VTN Coordinator
with virtual network functions. The requirements for installing these
two are different.Therefore, we recommend that you install VTN Manager
and VTN Coordinator in different machines.

List of installation Troubleshooting How to’s
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  https://wiki.opendaylight.org/view/OpenDaylight_Virtual_Tenant_Network_(VTN):Installation:VTN_Coordinator

**After executing db\_setup, you have encountered the error "Failed to
setup database"?**

The error could be due to the below reasons \* Access Restriction

The user who owns /usr/local/vtn/ directory and installs VTN
Coordinator, can only start db\_setup. Example :

::

      The directory should appear as below (assuming the user as "vtn"):
      # ls -l /usr/local/
        drwxr-xr-x. 12 vtn  vtn  4096 Mar 14 21:53 vtn
      If the user doesnot own /usr/local/vtn/ then, please run the below command (assuming the username as vtn),
                  chown -R vtn:vtn /usr/local/vtn

-  Postgres not Present

::

    1. In case of Fedora/CentOS/RHEL, please check if /usr/pgsql/<version> directory is present and also ensure the commands initdb, createdb,pg_ctl,psql are working. If, not please re-install postgres packages
    2. In case of Ubuntu, check if /usr/lib/postgres/<version> directory is present and check for the commands as in the previous step.

-  Not enough space to create tables

::

    Please check df -k and ensure enough free space is available.

-  If the above steps do not solve the problem, please refer to the log
   file for the exact problem

::

    /usr/local/vtn/var/dbm/unc_setup_db.log for the exact error.

-  list of VTN Coordinator processes

-  Run the below command ensure the Coordinator daemons are running.

::

           Command:     /usr/local/vtn/bin/unc_dmctl status
           Name              Type           IPC Channel       PID
        -----------       -----------      --------------     ------
            drvodcd         DRIVER           drvodcd           15972
            lgcnwd         LOGICAL           lgcnwd            16010
            phynwd         PHYSICAL          phynwd            15996

-  Issue the curl command to fetch version and ensure the process is
   able to respond.

**How to debug a startup failure?.**

The following activities take place in order during startup

-  Database server is started after setting virtual memory to required
   value,Any database startup errors will be reflected in any of the
   below logs.

::

             /usr/local/vtn/var/dbm/unc_db_script.log.
             /usr/local/vtn/var/db/pg_log/postgresql-*.log (the pattern will have the date)

-  uncd daemon is kicked off, The daemon in turn kicks off the rest of
   the daemons.

::

      Any  uncd startup failures will be reflected in /usr/local/vtn/var/uncd/uncd_start.err.

After setting up the apache tomcat server, what are the aspects that should be checked.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

**Please check if catalina is running..**

::

        The command ps -ef | grep catalina | grep -v grep should list a catalina process

**If you encounter an erroneous situation where the REST API is always
failing..**

::

      Please ensure the firewall settings for port:8282(Lithium release) or port:8083(Post Lithium release) and enable the same.

**How to debug a REST API returning a failure message?.**

Please check the /usr/share/java/apache-tomcat-7.0.39/logs/core/core.log
for failure details.

**REST API for VTN configuration fails, how to debug?.**

The default log level for all daemons is "INFO", to debug the situation
TRACE or DEBUG logs may be needed. To increase the log level for
individual daemons, please use the commands suggested below

::

      /usr/local/vtn/bin/lgcnw_control loglevel trace -- upll daemon log
       /usr/local/vtn/bin/phynw_control loglevel trace -- uppl daemon log
       /usr/local/vtn/bin/unc_control loglevel trace -- uncd daemon log
       /usr/local/vtn/bin/drvodc_control loglevel trace -- Driver daemon log

After setting the log levels, the operation can be repeated and the log
files can be referred for debugging.

**Problems while Installing PostgreSQL due to openssl.**

Errors may occur when trying to install postgreSQL rpms. Recently
PostgreSQL has upgraded all their binaries to use the latest openssl
versions with fix for http://en.wikipedia.org/wiki/Heartbleed Please
upgrade the openssl package to the latest version and re-install. For
RHEL 6.1/6.4 : If you have subscription, Please use the same and update
the rpms. The details are available in the following link
https://access.redhat.com/site/solutions/781793 ACCESS-REDHAT

::

      rpm -Uvh http://mirrors.kernel.org/centos/6/os/x86_64/Packages/openssl-1.0.1e-15.el6.x86_64.rpm
      rpm -ivh http://mirrors.kernel.org/centos/6/os/x86_64/Packages/openssl-devel-1.0.1e-15.el6.x86_64.rpm

For other linux platforms, Please do yum update, the public respositroes
will have the latest openssl, please install the same.

Support for Microsoft SCVMM 2012 R2 with ODL VTN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Introduction
^^^^^^^^^^^^

System Center Virtual Machine Manager (SCVMM) is Microsoft’s virtual
machine support center for window’s based emulations. SCVMM is a
management solution for the virtualized data center. You can use it to
configure and manage your virtualization host, networking, and storage
resources in order to create and deploy virtual machines and services to
private clouds that you have created.

The VSEM Provider is a plug-in to bridge between SCVMM and OpenDaylight.

Microsoft Hyper-V is a server virtualization developed by Microsoft,
which provides virtualization services through hypervisor-based
emulations.

.. figure:: ./images/vtn/setup_diagram_SCVMM.png
   :alt: Set-Up Diagram

   Set-Up Diagram

**The topology used in this set-up is:**

-  A SCVMM with VSEM Provider installed and a running VTN Coordinator
   and OpenDaylight with VTN Feature installed.

-  PF1000 virtual switch extension has been installed in the two Hyper-V
   servers as it implements the OpenFlow capability in Hyper-V.

-  Three OpenFlow switches simulated using mininet and connected to
   Hyper-V.

-  Four VM’s hosted using SCVMM.

**It is implemented as two major components:**

-  SCVMM

-  OpenDaylight (VTN Feature)

   -  VTN Coordinator

VTN Coordinator
^^^^^^^^^^^^^^^

OpenDaylight VTN as Network Service provider for SCVMM where VSEM
provider is added in the Network Service which will handle all requests
from SCVMM and communicate with the VTN Coordinator. It is used to
manage the network virtualization provided by OpenDaylight.

Installing HTTPS in VTN Coordinator
'''''''''''''''''''''''''''''''''''

-  System Center Virtual Machine Manager (SCVMM) supports only https
   protocol.

**Apache Portable Runtime (APR) Installation Steps**

-  Enter the command "yum install **apr**" in VTN Coordinator installed
   machine.

-  In /usr/bin, create a soft link as "ln –s /usr/bin/apr-1-config
   /usr/bin/apr-config".

-  Extract tomcat under "/usr/share/java" by using the below command
   "tar -xvf apache-tomcat-7.0.56.tar.gz –C /usr/share/java".

    **Note**

    Please go through the bleow link to download
    apache-tomcat-7.0.56.tar.gz file,
    https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.56/bin/

-  Please go to the directory "cd
   /usr/share/java/apache-tomcat-7.0.56/bin and unzip tomcat-native.gz
   using this command "tar -xvf tomcat-native.gz".

-  Go to the directory "cd
   /usr/share/java/apache-tomcat-7.0.56/bin/tomcat-native-1.1.27-src/jni/native".

-  Enter the command "./configure --with-apr=/usr/bin/apr-config".

-  Enter the command "make" and "make install".

-  Apr libraries are successfully installed in "/usr/local/apr/lib".

**Enable HTTP/HTTPS in VTN Coordinator**

Enter the command "system-config-firewall-tui" to enable firewall
settings in server.

**Create a CA’s private key and a self-signed certificate in server**

-  Execute the following command "openssl req -x509 -days 365
   -extensions v3\_ca -newkey rsa:2048 –out /etc/pki/CA/cacert.pem
   –keyout /etc/pki/CA/private/cakey.pem" in a single line.

+-----------------------+----------------------------------------------------+
| Argument              | Description                                        |
+=======================+====================================================+
| Country Name          | | Specify the country code.                        |
|                       | | For example, JP                                  |
+-----------------------+----------------------------------------------------+
| State or Province     | | Specify the state or province.                   |
| Name                  | | For example, Tokyo                               |
+-----------------------+----------------------------------------------------+
| Locality Name         | | Locality Name                                    |
|                       | | For example, Chuo-Ku                             |
+-----------------------+----------------------------------------------------+
| Organization Name     | Specify the company.                               |
+-----------------------+----------------------------------------------------+
| Organizational Unit   | Specify the department, division, or the like.     |
| Name                  |                                                    |
+-----------------------+----------------------------------------------------+
| Common Name           | Specify the host name.                             |
+-----------------------+----------------------------------------------------+
| Email Address         | Specify the e-mail address.                        |
+-----------------------+----------------------------------------------------+

-  Execute the following commands: "touch /etc/pki/CA/index.txt" and
   "echo 00 > /etc/pki/CA/serial" in server after setting your CA’s
   private key.

**Create a private key and a CSR for web server**

-  Execute the following command "openssl req -new -newkey rsa:2048 -out
   csr.pem –keyout /usr/local/vtn/tomcat/conf/key.pem" in a single line.

-  Enter the PEM pass phrase: Same password you have given in CA’s
   private key PEM pass phrase.

+-----------------------+----------------------------------------------------+
| Argument              | Description                                        |
+=======================+====================================================+
| Country Name          | | Specify the country code.                        |
|                       | | For example, JP                                  |
+-----------------------+----------------------------------------------------+
| State or Province     | | Specify the state or province.                   |
| Name                  | | For example, Tokyo                               |
+-----------------------+----------------------------------------------------+
| Locality Name         | | Locality Name                                    |
|                       | | For example, Chuo-Ku                             |
+-----------------------+----------------------------------------------------+
| Organization Name     | Specify the company.                               |
+-----------------------+----------------------------------------------------+
| Organizational Unit   | Specify the department, division, or the like.     |
| Name                  |                                                    |
+-----------------------+----------------------------------------------------+
| Common Name           | Specify the host name.                             |
+-----------------------+----------------------------------------------------+
| Email Address         | Specify the e-mail address.                        |
+-----------------------+----------------------------------------------------+
| A challenge password  | Specify the challenge password.                    |
+-----------------------+----------------------------------------------------+
| An optional company   | Specify an optional company name.                  |
| name                  |                                                    |
+-----------------------+----------------------------------------------------+

**Create a certificate for web server**

-  Execute the following command "openssl ca –in csr.pem –out
   /usr/local/vtn/tomcat/conf/cert.pem –days 365 –batch" in a single
   line.

-  Enter pass phrase for /etc/pki/CA/private/cakey.pem: Same password
   you have given in CA’s private key PEM pass phrase.

-  Open the tomcat file using "vim /usr/local/vtn/tomcat/bin/tomcat".

-  Include the line " TOMCAT\_PROPS="$TOMCAT\_PROPS
   -Djava.library.path=\\"/usr/local/apr/lib\\"" " in 131th line and
   save the file.

**Edit server.xml file and restart the server**

-  Open the server.xml file using "vim
   /usr/local/vtn/tomcat/conf/server.xml" and add the below lines.

   ::

       <Connector port="${vtn.port}" protocol="HTTP/1.1" SSLEnabled="true"
       maxThreads="150" scheme="https" secure="true"
       SSLCertificateFile="/usr/local/vtn/tomcat/conf/cert.pem"
       SSLCertificateKeyFile="/usr/local/vtn/tomcat/conf/key.pem"
       SSLPassword=same password you have given in CA's private key PEM pass phrase
       connectionTimeout="20000" />

-  Save the file and restart the server.

-  To stop vtn use the following command.

   ::

       /usr/local/vtn/bin/vtn_stop

-  To start vtn use the following command.

   ::

       /usr/local/vtn/bin/vtn_start

-  Copy the created CA certificate from cacert.pem to cacert.crt by
   using the following command,

   ::

       openssl x509 –in /etc/pki/CA/cacert.pem –out cacert.crt

   **Checking the HTTP and HTTPS connection from client**

-  You can check the HTTP connection by using the following command:

   ::

       curl -X GET -H 'contenttype:application/json' -H 'username:admin' -H 'password:adminpass' http://<server IP address>:8083/vtn-webapi/api_version.json

-  You can check the HTTPS connection by using the following command:

   ::

       curl -X GET -H 'contenttype:application/json' -H 'username:admin' -H 'password:adminpass' https://<server IP address>:8083/vtn-webapi/api_version.json --cacert /etc/pki/CA/cacert.pem

-  The response should be like this for both HTTP and HTTPS:

   ::

       {"api_version":{"version":"V1.2"}}

Prerequisites to create Network Service in SCVMM machine, Please follow the below steps
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.  Please go through the below link to download VSEM Provider zip file,
    https://nexus.opendaylight.org/content/groups/public/org/opendaylight/vtn/application/vtnmanager-vsemprovider/1.0.0-Lithium/vtnmanager-vsemprovider-1.0.0-Lithium-bin.zip

2.  Unzip the vtnmanager-vsemprovider-1.0.0-Lithium-bin.zip file
    anywhere in your SCVMM machine.

3.  Stop SCVMM service from **"service manager→tools→servers→select
    system center virtual machine manager"** and click stop.

4.  Go to **"C:/Program Files"** in your SCVMM machine. Inside
    **"C:/Program Files"**, create a folder named as \*"ODLProvider".

5.  Inside **"C:/Program Files/ODLProvider"**, create a folder named as
    "Module" in your SCVMM machine.

6.  Inside "C:/Program Files/ODLProvider/Module", Create two folders
    named as **"Odl.VSEMProvider"** and **"VSEMOdlUI"** in your SCVMM
    machine.

7.  Copy the **"VSEMOdl.dll"** file from
    **"ODL\_SCVMM\_PROVIDER/ODL\_VSEM\_PROVIDER"** to **"C:/Program
    Files/ODLProvider/Module/Odl.VSEMProvider"** in your SCVMM machine.

8.  Copy the **"VSEMOdlProvider.psd1"** file from
    **"application/vsemprovider/VSEMOdlProvider/VSEMOdlProvider.psd1"**
    to **"C:/Program Files/ODLProvider/Module/Odl.VSEMProvider"** in
    your SCVMM machine.

9.  Copy the **"VSEMOdlUI.dll"** file from
    **"ODL\_SCVMM\_PROVIDER/ODL\_VSEM\_PROVIDER\_UI"** to **"C:/Program
    Files/ODLProvider/Module/VSEMOdlUI"** in your SCVMM machine.

10. Copy the **"VSEMOdlUI.psd1"** file from
    **"application/vsemprovider/VSEMOdlUI"** to **"C:/Program
    Files/ODLProvider/Module/VSEMOdlUI"** in your SCVMM machine.

11. Copy the **"reg\_entry.reg"** file from
    **"ODL\_SCVMM\_PROVIDER/Register\_settings"** to your SCVMM desktop
    and double click the **"reg\_entry.reg"** file to install registry
    entry in your SCVMM machine.

12. Download **"PF1000.msi"** from this link,
    https://www.pf-info.com/License/en/index.php?url=index/index_non_buyer
    and place into **"C:/Program Files/Switch Extension Drivers"** in
    your SCVMM machine.

13. Start SCVMM service from **"service manager→tools→servers→select
    system center virtual machine manager"** and click start.

System Center Virtual Machine Manager (SCVMM)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It supports two major features:

-  Failover Clustering

-  Live Migration

Failover Clustering
'''''''''''''''''''

A single Hyper-V can host a number of virtual machines. If the host were
to fail then all of the virtual machines that are running on it will
also fail, thereby resulting in a major outage. Failover clustering
treats individual virtual machines as clustered resources. If a host
were to fail then clustered virtual machines are able to fail over to a
different Hyper-V server where they can continue to run.

Live Migration
''''''''''''''

Live Migration is used to migrate the running virtual machines from one
Hyper-V server to another Hyper-V server without any interruptions.
Please go through the below video for more details,

-  https://youtu.be/34YMOTzbNJM

SCVMM User Guide
^^^^^^^^^^^^^^^^

-  Please go through the below link for SCVMM user guide:
   https://wiki.opendaylight.org/images/c/ca/ODL_SCVMM_USER_GUIDE_final.pdf

-  Please go through the below links for more details

   -  OpenDaylight SCVMM VTN Integration: https://youtu.be/iRt4dxtiz94

   -  OpenDaylight Congestion Control with SCVMM VTN:
      https://youtu.be/34YMOTzbNJM

NETCONF User Guide
==================

Overview
--------

NETCONF is an XML based protocol used for configuration and monitoring
of devices in the network. The base NETCONF protocol is described in
`RFC-6241 <http://tools.ietf.org/html/rfc6241>`__.

**NETCONF in OpenDaylight:.**

OpenDaylight controller supports NETCONF protocol as a northbound server
as well as a southbound plugin.

Southbound (netconf-connector)
------------------------------

NETCONF southbound plugin is capable of connecting to remote NETCONF
devices and expose their configuration/operational datastores, rpcs and
notifications as MD-SAL mount points. These mount points allow
applications and remote users (over RESTCONF) to interact with the
mounted devices.

In terms of RFCs, the connector supports:

-  `RFC-6241 <http://tools.ietf.org/html/rfc6241>`__,

-  `RFC-5277 <https://tools.ietf.org/html/rfc5277>`__,

-  `RFC-6022 <https://tools.ietf.org/html/rfc6022>`__,

**Netconf-connector is fully model driven (utilising YANG modeling
language) so in addition to the above RFCs, it supports any
data/RPC/notifications described by a YANG model that is implemented by
the device.**

    **Tip**

    NETCONF southbound can be activated by installing
    ``odl-netconf-connector-all`` Karaf feature.

Netconf-connector configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are 2 ways for configuring netconf-connector (as is for any other
module) NETCONF or RESTCONF. This guide focuses on using RESTCONF.

Default configuration
^^^^^^^^^^^^^^^^^^^^^

The default configuration contains all the necessary dependencies (file:
01-netconf.xml) and a single instance of netconf-connector (file:
99-netconf-connector.xml) called **controller-config** which connects
itself to the NETCONF northbound in OpenDaylight in a loopback fashion.
The connector mounts the NETCONF server for config-subsystem in order to
enable RESTCONF protocol for config-subsystem. This RESTCONF still goes
via NETCONF, but using RESTCONF is much more user friendly than using
NETCONF.

Spawning additional netconf-connectors while the controller is running
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Preconditions:

1. OpenDaylight is running

2. In Karaf, you must have the netconf-connector installed (at the Karaf
   prompt, type: feature:install odl-netconf-connector-all); the
   loopback NETCONF mountpoint will be automatically configured and
   activated

3. Wait until log displays following entry:
   RemoteDevice{controller-config}: NETCONF connector initialized
   successfully

To configure a new netconf-connector you need to send following request
to RESTCONF:

POST
http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules

**Headers**: Accept application/xml Content-Type application/xml

::

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
      <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">prefix:sal-netconf-connector</type>
      <name>new-netconf-device</name>
      <address xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">127.0.0.1</address>
      <port xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">830</port>
      <username xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">admin</username>
      <password xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">admin</password>
      <tcp-only xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">false</tcp-only>
      <event-executor xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:netty">prefix:netty-event-executor</type>
        <name>global-event-executor</name>
      </event-executor>
      <binding-registry xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:md:sal:binding">prefix:binding-broker-osgi-registry</type>
        <name>binding-osgi-broker</name>
      </binding-registry>
      <dom-registry xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:md:sal:dom">prefix:dom-broker-osgi-registry</type>
        <name>dom-broker</name>
      </dom-registry>
      <client-dispatcher xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:config:netconf">prefix:netconf-client-dispatcher</type>
        <name>global-netconf-dispatcher</name>
      </client-dispatcher>
      <processing-executor xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:threadpool">prefix:threadpool</type>
        <name>global-netconf-processing-executor</name>
      </processing-executor>
      <keepalive-executor xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:threadpool">prefix:scheduled-threadpool</type>
        <name>global-netconf-ssh-scheduled-executor</name>
      </keepalive-executor>
    </module>

This spawns a new netconf-connector which tries to connect to (or mount)
a NETCONF device at 127.0.0.1 and port 830. You can check the
configuration of config-subsystem’s configuration datastore. The new
netconf-connector will now be present there. Just invoke:

GET
http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules

The response will contain the module for new-netconf-device.

Right after the new netconf-connector is created, it writes some useful
metadata into the datastore of MD-SAL under the network-topology
subtree. This metadata can be found at:

GET
http://localhost:8181/restconf/operational/network-topology:network-topology/

Information about connection status, device capabilities etc. can be
found there.

Connecting to a device not supporting NETCONF monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The netconf-connector in OpenDaylight relies on ietf-netconf-monitoring
support when connecting to remote NETCONF device. The
ietf-netconf-monitoring support allows netconf-connector to list and
download all YANG schemas that are used by the device. NETCONF connector
can only communicate with a device if it knows the set of used schemas
(or at least a subset). However, some devices use YANG models internally
but do not support NETCONF monitoring. Netconf-connector can also
communicate with these devices, but you have to side load the necessary
yang models into OpenDaylight’s YANG model cache for netconf-connector.
In general there are 2 situations you might encounter:

**1. NETCONF device does not support ietf-netconf-monitoring but it does
list all its YANG models as capabilities in HELLO message**

This could be a device that internally uses only ietf-inet-types YANG
model with revision 2010-09-24. In the HELLO message that is sent from
this device there is this capability reported:

::

    urn:ietf:params:xml:ns:yang:ietf-inet-types?module=ietf-inet-types&revision=2010-09-24

**For such devices you only need to put the schema into folder
cache/schema inside your Karaf distribution.**

    **Important**

    The file with YANG schema for ietf-inet-types has to be called
    ietf-inet-types@2010-09-24.yang. It is the required naming format of
    the cache.

**2. NETCONF device does not support ietf-netconf-monitoring and it does
NOT list its YANG models as capabilities in HELLO message**

Compared to device that lists its YANG models in HELLO message, in this
case there would be no capability with ietf-inet-types in the HELLO
message. This type of device basically provides no information about the
YANG schemas it uses so its up to the user of OpenDaylight to properly
configure netconf-connector for this device.

Netconf-connector has an optional configuration attribute called
yang-module-capabilities and this attribute can contain a list of "YANG
module based" capabilities. So by setting this configuration attribute,
it is possible to override the "yang-module-based" capabilities reported
in HELLO message of the device. To do this, we need to modify the
configuration of netconf-connector by adding this xml (It needs to be
added next to the address, port, username etc. configuration elements):

::

    <yang-module-capabilities xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
      <capability xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        urn:ietf:params:xml:ns:yang:ietf-inet-types?module=ietf-inet-types&amp;revision=2010-09-24
      </capability>
    </yang-module-capabilities>

**Remember to also put the YANG schemas into the cache folder.**

    **Note**

    For putting multiple capabilities, you just need to replicate the
    capability xml element inside yang-module-capability element.
    Capability element is modeled as a leaf-list. With this
    configuration, we would make the remote device report usage of
    ietf-inet-types in the eyes of netconf-connector.

Reconfiguring Netconf-Connector While the Controller is Running
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is possible to change the configuration of a running module while the
whole controller is running. This example will continue where the last
left off and will change the configuration for the brand new
netconf-connector after it was spawned. Using one RESTCONF request, we
will change both username and password for the netconf-connector.

To update an existing netconf-connector you need to send following
request to RESTCONF:

PUT
http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules/module/odl-sal-netconf-connector-cfg:sal-netconf-connector/new-netconf-device

::

    <module xmlns="urn:opendaylight:params:xml:ns:yang:controller:config">
      <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">prefix:sal-netconf-connector</type>
      <name>new-netconf-device</name>
      <username xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">bob</username>
      <password xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">passwd</password>
      <tcp-only xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">false</tcp-only>
      <event-executor xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:netty">prefix:netty-event-executor</type>
        <name>global-event-executor</name>
      </event-executor>
      <binding-registry xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:md:sal:binding">prefix:binding-broker-osgi-registry</type>
        <name>binding-osgi-broker</name>
      </binding-registry>
      <dom-registry xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:md:sal:dom">prefix:dom-broker-osgi-registry</type>
        <name>dom-broker</name>
      </dom-registry>
      <client-dispatcher xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:config:netconf">prefix:netconf-client-dispatcher</type>
        <name>global-netconf-dispatcher</name>
      </client-dispatcher>
      <processing-executor xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:threadpool">prefix:threadpool</type>
        <name>global-netconf-processing-executor</name>
      </processing-executor>
      <keepalive-executor xmlns="urn:opendaylight:params:xml:ns:yang:controller:md:sal:connector:netconf">
        <type xmlns:prefix="urn:opendaylight:params:xml:ns:yang:controller:threadpool">prefix:scheduled-threadpool</type>
        <name>global-netconf-ssh-scheduled-executor</name>
      </keepalive-executor>
    </module>

Since a PUT is a replace operation, the whole configuration must be
specified along with the new values for username and password. This
should result in a 2xx response and the instance of netconf-connector
called new-netconf-device will be reconfigured to use username bob and
password passwd. New configuration can be verified by executing:

GET
http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules/module/odl-sal-netconf-connector-cfg:sal-netconf-connector/new-netconf-device

With new configuration, the old connection will be closed and a new one
established.

Destroying Netconf-Connector While the Controller is Running
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using RESTCONF one can also destroy an instance of a module. In case of
netconf-connector, the module will be destroyed, NETCONF connection
dropped and all resources will be cleaned. To do this, simply issue a
request to following URL:

DELETE
http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/controller-config/yang-ext:mount/config:modules/module/odl-sal-netconf-connector-cfg:sal-netconf-connector/new-netconf-device

The last element of the URL is the name of the instance and its
predecessor is the type of that module (In our case the type is
**sal-netconf-connector** and name **new-netconf-device**). The type and
name are actually the keys of the module list.

Netconf-connector utilisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the connector is up and running, users can utilize the new Mount
point instance. By using RESTCONF or from their application code. This
chapter deals with using RESTCONF and more information for app
developers can be found in the developers guide or in the official
tutorial application **ncmount** that can be found in the coretutorials
project:

-  https://github.com/opendaylight/coretutorials/tree/stable/lithium/ncmount

Reading data from the device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Just invoke (no body needed):

GET
http://localhost:8080/restconf/operational/network-topology:network-topology/topology/topology-netconf/node/new-netconf-device/yang-ext:mount/

This will return the entire content of operation datastore from the
device. To view just the configuration datastore, change **operational**
in this URL to **config**.

Writing configuration data to the device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In general, you cannot simply write any data you want to the device. The
data have to conform to the YANG models implemented by the device. In
this example we are adding a new interface-configuration to the mounted
device (assuming the device supports Cisco-IOS-XR-ifmgr-cfg YANG model).
In fact this request comes from the tutorial dedicated to the
**ncmount** tutorial app.

POST
http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/new-netconf-device/yang-ext:mount/Cisco-IOS-XR-ifmgr-cfg:interface-configurations

::

    <interface-configuration xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
        <active>act</active>
        <interface-name>mpls</interface-name>
        <description>Interface description</description>
        <bandwidth>32</bandwidth>
        <link-status></link-status>
    </interface-configuration>

Should return 200 response code with no body.

    **Tip**

    This call is transformed into a couple of NETCONF RPCs. Resulting
    NETCONF RPCs that go directly to the device can be found in the
    OpenDaylight logs after invoking ``log:set TRACE
    org.opendaylight.controller.sal.connect.netconf`` in the Karaf
    shell. Seeing the NETCONF RPCs might help with debugging.

This request is very similar to the one where we spawned a new netconf
device. That’s because we used the loopback netconf-connector to write
configuration data into config-subsystem datastore and config-subsystem
picked it up from there.

Invoking custom RPC
^^^^^^^^^^^^^^^^^^^

Devices can implement any additional RPC and as long as it provides YANG
models for it, it can be invoked from OpenDaylight. Following example
shows how to invoke the get-schema RPC (get-schema is quite common among
netconf devices). Invoke:

POST
http://localhost:8181/restconf/operations/network-topology:network-topology/topology/topology-netconf/node/new-netconf-device/yang-ext:mount/ietf-netconf-monitoring:get-schema

::

    <input xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring">
      <identifier>ietf-yang-types</identifier>
      <version>2013-07-15</version>
    </input>

This call should fetch the source for ietf-yang-types YANG model from
the mounted device.

Netconf-connector + Netopeer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Netopeer <https://github.com/cesnet/netopeer>`__ (an open-source
NETCONF server) can be used for testing/exploring NETCONF southbound in
OpenDaylight.

Netopeer installation
^^^^^^^^^^^^^^^^^^^^^

`Docker <https://www.docker.com/>`__ container with netopeer will be
used in this guid. To install docker and start the `netopeer
image <https://index.docker.io/u/dockeruser/netopeer/>`__ perform
following steps:

1. Install docker http://docs.docker.com/linux/step_one/

2. Start the netopeer image:

   ::

       docker run -rm -t -p 1831:830 dockeruser/netopeer

3. Verify netopeer is running by invoking (netopeer should send its
   HELLO message right away:

   ::

       ssh root@localhost -p 1831 -s netconf
       (password root)

Mounting netopeer NETCONF server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Preconditions:

-  OpenDaylight is started with features ``odl-restconf-all`` and
   ``odl-netconf-connector-all``.

-  Netopeer is up and running in docker

Now just follow the chapter: `Spawning
netconf-connector <#_spawning_additional_netconf_connectors_while_the_controller_is_running>`__.
In the payload change the:

-  name to e.g. netopeer

-  usernam/password to your system credentials

-  ip to localhost

-  port to 1831.

After netopeer is mounted successfully, its configuration can be read
using RESTCONF by invoking:

GET
http://localhost:8181/restconf/config/network-topology:network-topology/topology/topology-netconf/node/netopeer/yang-ext:mount/

Northbound (NETCONF servers)
----------------------------

OpenDaylight provides 2 types of NETCONF servers:

-  **NETCONF server for config-subsystem(listening by default on port
   1830)**

   -  Serves as a default interface for config-subsystem and allows
      users to spawn/reconfigure/destroy modules(or applications) in
      OpenDaylight

-  **NETCONF server for MD-SAL(listening by default on port 2830)**

   -  Serves as an alternative interface for MD-SAL (besides RESTCONF)
      and allows users to read/write data from MD-SAL’s datastore and to
      invoke its rpcs (NETCONF notifications are not available in the
      Lithium release of OpenDaylight)

    **Note**

    The reason for having 2 NETCONF servers is that config-subsystem and
    MD-SAL are 2 different components of OpenDaylight and require
    different approach for NETCONF message handling and data
    translation. These 2 components will probably merge in the future.

NETCONF server for config-subsystem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This NETCONF server is the primary interface for config-subsystem. It
allows the users to interact with config-subsystem in a standardized
NETCONF manner.

In terms of RFCs, these are supported:

-  `RFC-6241 <http://tools.ietf.org/html/rfc6241>`__,

-  `RFC-5277 <https://tools.ietf.org/html/rfc5277>`__,

-  `RFC-6470 <https://tools.ietf.org/html/rfc6470>`__

   -  (partially, only the schema-change notification is available in
      Lithium release)

-  `RFC-6022 <https://tools.ietf.org/html/rfc6022>`__,

For regular users it is recommended to use RESTCONF + the
controller-config loopback mountpoint instead of using pure NETCONF. How
to do that is spesific for each component/module/application in
OpenDaylight and can be found in their dedicated user guides

NETCONF server for MD-SAL
~~~~~~~~~~~~~~~~~~~~~~~~~

This NETCONF server is just a generic interface to MD-SAL in
OpenDaylight. It uses the stadard MD-SAL APIs and serves as an
alternative to RESTCONF. It is fully model driven and supports any data
and rpcs that are supported by MD-SAL.

In terms of RFCs, these are supported:

-  `RFC-6241 <http://tools.ietf.org/html/rfc6241>`__,

-  `RFC-6022 <https://tools.ietf.org/html/rfc6022>`__,

Notifications over NETCONF are not supported in the Lithium release.

    **Tip**

    Install NETCONF northbound for MD-SAL by installing feature:
    ``odl-netconf-mdsal`` in karaf. Default binding port is **2830**.

Configuration
^^^^^^^^^^^^^

The default configuration can be found in file: *08-netconf-mdsal.xml*.
The file contains the configuration for all necessary dependencies and a
single SSH endpoint starting on port 2830. There is also a (by default
disabled) TCP endpoint. It is possible to start multiple endpoints at
the same time either in the initial configuration file or while
OpenDaylight is running.

The credentials for SSH endpoint can also be configured here, the
defaults are admin/admin. Credentials in the SSH endpoint are not yet
managed by the centralized AAA component and have to be configured
separately.

Verifying MD-SAL’s NETCONF server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After the NETCONF server is available it can be examined by e.g. a
command line ssh tool:

::

    ssh admin@localhost -p 2830 -s netconf

The server will respond by sending its HELLO message and can be used as
a regular NETCONF server from now on.

Mounting the MD-SAL’s NETCONF server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To perform this operation, just spawn a new netconf-connector as
described in `Spawning
netconf-connector <#_spawning_additional_netconf_connectors_while_the_controller_is_running>`__.
Just change the ip to "127.0.0.1" port to "2830" and its name to
"controller-mdsal".

Now the MD-SAL’s datastore can be read over RESTCONF via NETCONF by
invoking:

GET
http://localhost:8181/restconf/operational/network-topology:network-topology/topology/topology-netconf/node/controller-mdsal/yang-ext:mount

    **Note**

    This might not seem very useful, since MD-SAL can be accessed
    directly from RESTCONF or from Application code, but the same method
    can be used to mount and control other OpenDaylight instances by the
    "master OpenDaylight".

NETCONF testtool
----------------

**NETCONF testtool is a set of standalone runnable jars that can:**

-  Simulate NETCONF devices(suitable for scale testing)

-  Stress/Performance test NETCONF devices

-  Stress/Performance test RESTCONF devices

These jars are part of OpenDaylight’s controller project and are built
from the NETCONF codebase in OpenDaylight.

    **Tip**

    Download testtool from OpenDaylight Nexus at:
    http://nexus.opendaylight.org/#nexus-search;quick~netconf-testtool

**Nexus contains 3 executable tools:**

-  executable.jar - device simulator

-  stress.client.tar.gz - NETCONF stress/performance measuring tool

-  perf-client.jar - RESTCONF stress/performance measuring tool

    **Tip**

    Each executable tool provides help. Just invoke ``java -jar
    <name-of-the-tool.jar> --help``

NETCONF device simulator
~~~~~~~~~~~~~~~~~~~~~~~~

Detailed information for NETCONF device simulator can be found at:
https://wiki.opendaylight.org/view/OpenDaylight_Controller:Netconf:Testtool

NETCONF stress/performance measuring tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is basically a NETCONF client that puts NETCONF servers under heavy
load of NETCONF RPCs and measures the time until a configurable amount
of them is processed.

RESTCONF stress-performance measuring tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Very similar to NETCONF stress tool with the difference of using
RESTCONF protocol instead of NETCONF.

YANG-PUSH
=========

This section describes how to use the YANG-PUSH feature in OpenDaylight
and contains contains configuration, administration, and management
sections for the feature.

Overview
--------

YANG PUBSUB project allows applications to place subscriptions upon
targeted subtrees of YANG datastores residing on remote devices. Changes
in YANG objects within the remote subtree can be pushed to an
OpenDaylight MD-SAL and to the application as specified without a
requiring the controller to make a continuous set of fetch requests.

YANG-PUSH capabilities available
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the base code which embodies the intent of
YANG-PUSH requirements for subscription as defined in
{i2rs-pub-sub-requirements}
[https://datatracker.ietf.org/doc/draft-ietf-i2rs-pub-sub-requirements/].
The mechanism for delivering on these YANG-PUSH requirements over
Netconf transport is defined in {netconf-yang-push} [netconf-yang-push:
https://tools.ietf.org/html/draft-ietf-netconf-yang-push-00].

Note that in the current release, not all capabilities of
draft-ietf-netconf-yang-push are realized. Currently only implemented is
**create-subscription** RPC support from
ietf-datastore-push@2015-10-15.yang; and this will be for periodic
subscriptions only. There of course is intent to provide much additional
functionality in future OpenDaylight releases.

Future YANG-PUSH capabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Over time, the intent is to flesh out more robust capabilities which
will allow OpenDaylight applications to subscribe to YANG-PUSH compliant
devices. Capabilities for future releases will include:

Support for subscription change/delete: **modify-subscription** rpc
support for all mountpoint devices or particular mountpoint device
**delete-subscription** rpc support for all mountpoint devices or
particular mountpoint device

Support for static subscriptions: This will enable the receipt of
subscription updates pushed from publishing devices where no signaling
from the controller has been used to establish the subscriptions.

Support for additional transports: NETCONF is not the only transport of
interest to OpenDaylight or the subscribed devices. Over time this code
will support Restconf and HTTP/2 transport requirements defined in
{netconf-restconf-yang-push}
[https://tools.ietf.org/html/draft-voit-netconf-restconf-yang-push-01]

YANG-PUSH Architecture
----------------------

The code architecture of Yang push consists of two main elements

YANGPUSH Provider YANGPUSH Listener

YANGPUSH Provider receives create-subscription requests from
applications and then establishes/registers the corresponding listener
which will receive information pushed by a publisher. In addition,
YANGPUSH Provider also invokes an augmented OpenDaylight
create-subscription RPC which enables applications to register for
notification as per rfc5277. This augmentation adds periodic time period
(duration) and subscription-id values to the existing RPC parameters.
The Java package supporting this capability is
“org.opendaylight.yangpush.impl”. YangpushDomProvider is the class which
supports this YANGPUSH Provider capability.

The YANGPUSH Listener accepts update notifications from a device after
they have been de-encapsulated from the NETCONF transport. The YANGPUSH
Listener then passes these updates to MD-SAL. This function is
implemented via the YangpushDOMNotificationListener class within the
“org.opendaylight.yangpush.listner” Java package. Applications should
monitor MD-SAL for the availability of newly pushed subscription
updates.

YANG-PUSH Catalog
-----------------

The NF Catalog contains metadata describing a NF.

Configuring YANG-PUSH Catalog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD: Describe how to configure YANG-PUSH Catalog after installation.

Administering YANG-PUSH Catalog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD: Include related command reference or operations for using YANG-PUSH
Catalog.

YANG-PUSH Workload Manager
--------------------------

The Workload Manager defines RPCs to manage instances.

Configuring YANG-PUSH Workload Manager
--------------------------------------

TBD: Describe how to configure YANG-PUSH Workload Manager after
installation.

Administering YANG-PUSH Workload Manager
----------------------------------------

TBD: Include related command reference or operations for using YANG-PUSH
Workload Manager.

Tutorials
---------

Below are tutorials for YANG-PUSH.

Using YANG-PUSH Catalog
~~~~~~~~~~~~~~~~~~~~~~~

TBD: State the purpose of tutorial

Overview
^^^^^^^^

TBD: An overview of the YANG-PUSH Catalog tutorial

Prerequisites
^^^^^^^^^^^^^

TBD: Provide any prerequisite information, assumed knowledge, or
environment required to execute the use case.

Target Environment
^^^^^^^^^^^^^^^^^^

There are no topology requirement for using YANG-PUSH. A single node
able interact as per
https://tools.ietf.org/html/draft-ietf-netconf-yang-push-00 is
sufficient to use this capability.

Instructions
^^^^^^^^^^^^

TBD: Step by step procedure for using YANG-PUSH Catalog.

Using YANG-PUSH Workload Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD: State the purpose of tutorial

Overview
^^^^^^^^

TBD: An overview of the YANG-PUSH Workload Manager tutorial

Prerequisites
^^^^^^^^^^^^^

TBD: Provide any prerequisite information, assumed knowledge, or
environment required to execute the use case.

Target Environment
^^^^^^^^^^^^^^^^^^

TBD: Include any topology requirement for the use case.

Instructions
^^^^^^^^^^^^

TBD: Step by step procedure for using YANG-PUSH Workload Manager.
