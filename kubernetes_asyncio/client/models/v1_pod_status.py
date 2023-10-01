# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.27.6
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from kubernetes_asyncio.client.configuration import Configuration


class V1PodStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'conditions': 'list[V1PodCondition]',
        'container_statuses': 'list[V1ContainerStatus]',
        'ephemeral_container_statuses': 'list[V1ContainerStatus]',
        'host_ip': 'str',
        'init_container_statuses': 'list[V1ContainerStatus]',
        'message': 'str',
        'nominated_node_name': 'str',
        'phase': 'str',
        'pod_ip': 'str',
        'pod_ips': 'list[V1PodIP]',
        'qos_class': 'str',
        'reason': 'str',
        'resize': 'str',
        'start_time': 'datetime'
    }

    attribute_map = {
        'conditions': 'conditions',
        'container_statuses': 'containerStatuses',
        'ephemeral_container_statuses': 'ephemeralContainerStatuses',
        'host_ip': 'hostIP',
        'init_container_statuses': 'initContainerStatuses',
        'message': 'message',
        'nominated_node_name': 'nominatedNodeName',
        'phase': 'phase',
        'pod_ip': 'podIP',
        'pod_ips': 'podIPs',
        'qos_class': 'qosClass',
        'reason': 'reason',
        'resize': 'resize',
        'start_time': 'startTime'
    }

    def __init__(self, conditions=None, container_statuses=None, ephemeral_container_statuses=None, host_ip=None, init_container_statuses=None, message=None, nominated_node_name=None, phase=None, pod_ip=None, pod_ips=None, qos_class=None, reason=None, resize=None, start_time=None, local_vars_configuration=None):  # noqa: E501
        """V1PodStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._container_statuses = None
        self._ephemeral_container_statuses = None
        self._host_ip = None
        self._init_container_statuses = None
        self._message = None
        self._nominated_node_name = None
        self._phase = None
        self._pod_ip = None
        self._pod_ips = None
        self._qos_class = None
        self._reason = None
        self._resize = None
        self._start_time = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if container_statuses is not None:
            self.container_statuses = container_statuses
        if ephemeral_container_statuses is not None:
            self.ephemeral_container_statuses = ephemeral_container_statuses
        if host_ip is not None:
            self.host_ip = host_ip
        if init_container_statuses is not None:
            self.init_container_statuses = init_container_statuses
        if message is not None:
            self.message = message
        if nominated_node_name is not None:
            self.nominated_node_name = nominated_node_name
        if phase is not None:
            self.phase = phase
        if pod_ip is not None:
            self.pod_ip = pod_ip
        if pod_ips is not None:
            self.pod_ips = pod_ips
        if qos_class is not None:
            self.qos_class = qos_class
        if reason is not None:
            self.reason = reason
        if resize is not None:
            self.resize = resize
        if start_time is not None:
            self.start_time = start_time

    @property
    def conditions(self):
        """Gets the conditions of this V1PodStatus.  # noqa: E501

        Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions  # noqa: E501

        :return: The conditions of this V1PodStatus.  # noqa: E501
        :rtype: list[V1PodCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1PodStatus.

        Current service state of pod. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-conditions  # noqa: E501

        :param conditions: The conditions of this V1PodStatus.  # noqa: E501
        :type conditions: list[V1PodCondition]
        """

        self._conditions = conditions

    @property
    def container_statuses(self):
        """Gets the container_statuses of this V1PodStatus.  # noqa: E501

        The list has one entry per container in the manifest. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status  # noqa: E501

        :return: The container_statuses of this V1PodStatus.  # noqa: E501
        :rtype: list[V1ContainerStatus]
        """
        return self._container_statuses

    @container_statuses.setter
    def container_statuses(self, container_statuses):
        """Sets the container_statuses of this V1PodStatus.

        The list has one entry per container in the manifest. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status  # noqa: E501

        :param container_statuses: The container_statuses of this V1PodStatus.  # noqa: E501
        :type container_statuses: list[V1ContainerStatus]
        """

        self._container_statuses = container_statuses

    @property
    def ephemeral_container_statuses(self):
        """Gets the ephemeral_container_statuses of this V1PodStatus.  # noqa: E501

        Status for any ephemeral containers that have run in this pod.  # noqa: E501

        :return: The ephemeral_container_statuses of this V1PodStatus.  # noqa: E501
        :rtype: list[V1ContainerStatus]
        """
        return self._ephemeral_container_statuses

    @ephemeral_container_statuses.setter
    def ephemeral_container_statuses(self, ephemeral_container_statuses):
        """Sets the ephemeral_container_statuses of this V1PodStatus.

        Status for any ephemeral containers that have run in this pod.  # noqa: E501

        :param ephemeral_container_statuses: The ephemeral_container_statuses of this V1PodStatus.  # noqa: E501
        :type ephemeral_container_statuses: list[V1ContainerStatus]
        """

        self._ephemeral_container_statuses = ephemeral_container_statuses

    @property
    def host_ip(self):
        """Gets the host_ip of this V1PodStatus.  # noqa: E501

        IP address of the host to which the pod is assigned. Empty if not yet scheduled.  # noqa: E501

        :return: The host_ip of this V1PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this V1PodStatus.

        IP address of the host to which the pod is assigned. Empty if not yet scheduled.  # noqa: E501

        :param host_ip: The host_ip of this V1PodStatus.  # noqa: E501
        :type host_ip: str
        """

        self._host_ip = host_ip

    @property
    def init_container_statuses(self):
        """Gets the init_container_statuses of this V1PodStatus.  # noqa: E501

        The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status  # noqa: E501

        :return: The init_container_statuses of this V1PodStatus.  # noqa: E501
        :rtype: list[V1ContainerStatus]
        """
        return self._init_container_statuses

    @init_container_statuses.setter
    def init_container_statuses(self, init_container_statuses):
        """Sets the init_container_statuses of this V1PodStatus.

        The list has one entry per init container in the manifest. The most recent successful init container will have ready = true, the most recently started container will have startTime set. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-and-container-status  # noqa: E501

        :param init_container_statuses: The init_container_statuses of this V1PodStatus.  # noqa: E501
        :type init_container_statuses: list[V1ContainerStatus]
        """

        self._init_container_statuses = init_container_statuses

    @property
    def message(self):
        """Gets the message of this V1PodStatus.  # noqa: E501

        A human readable message indicating details about why the pod is in this condition.  # noqa: E501

        :return: The message of this V1PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1PodStatus.

        A human readable message indicating details about why the pod is in this condition.  # noqa: E501

        :param message: The message of this V1PodStatus.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def nominated_node_name(self):
        """Gets the nominated_node_name of this V1PodStatus.  # noqa: E501

        nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled.  # noqa: E501

        :return: The nominated_node_name of this V1PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._nominated_node_name

    @nominated_node_name.setter
    def nominated_node_name(self, nominated_node_name):
        """Sets the nominated_node_name of this V1PodStatus.

        nominatedNodeName is set only when this pod preempts other pods on the node, but it cannot be scheduled right away as preemption victims receive their graceful termination periods. This field does not guarantee that the pod will be scheduled on this node. Scheduler may decide to place the pod elsewhere if other nodes become available sooner. Scheduler may also decide to give the resources on this node to a higher priority pod that is created after preemption. As a result, this field may be different than PodSpec.nodeName when the pod is scheduled.  # noqa: E501

        :param nominated_node_name: The nominated_node_name of this V1PodStatus.  # noqa: E501
        :type nominated_node_name: str
        """

        self._nominated_node_name = nominated_node_name

    @property
    def phase(self):
        """Gets the phase of this V1PodStatus.  # noqa: E501

        The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:  Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.  More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase  # noqa: E501

        :return: The phase of this V1PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this V1PodStatus.

        The phase of a Pod is a simple, high-level summary of where the Pod is in its lifecycle. The conditions array, the reason and message fields, and the individual container status arrays contain more detail about the pod's status. There are five possible phase values:  Pending: The pod has been accepted by the Kubernetes system, but one or more of the container images has not been created. This includes time before being scheduled as well as time spent downloading images over the network, which could take a while. Running: The pod has been bound to a node, and all of the containers have been created. At least one container is still running, or is in the process of starting or restarting. Succeeded: All containers in the pod have terminated in success, and will not be restarted. Failed: All containers in the pod have terminated, and at least one container has terminated in failure. The container either exited with non-zero status or was terminated by the system. Unknown: For some reason the state of the pod could not be obtained, typically due to an error in communicating with the host of the pod.  More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#pod-phase  # noqa: E501

        :param phase: The phase of this V1PodStatus.  # noqa: E501
        :type phase: str
        """

        self._phase = phase

    @property
    def pod_ip(self):
        """Gets the pod_ip of this V1PodStatus.  # noqa: E501

        IP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated.  # noqa: E501

        :return: The pod_ip of this V1PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        """Sets the pod_ip of this V1PodStatus.

        IP address allocated to the pod. Routable at least within the cluster. Empty if not yet allocated.  # noqa: E501

        :param pod_ip: The pod_ip of this V1PodStatus.  # noqa: E501
        :type pod_ip: str
        """

        self._pod_ip = pod_ip

    @property
    def pod_ips(self):
        """Gets the pod_ips of this V1PodStatus.  # noqa: E501

        podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet.  # noqa: E501

        :return: The pod_ips of this V1PodStatus.  # noqa: E501
        :rtype: list[V1PodIP]
        """
        return self._pod_ips

    @pod_ips.setter
    def pod_ips(self, pod_ips):
        """Sets the pod_ips of this V1PodStatus.

        podIPs holds the IP addresses allocated to the pod. If this field is specified, the 0th entry must match the podIP field. Pods may be allocated at most 1 value for each of IPv4 and IPv6. This list is empty if no IPs have been allocated yet.  # noqa: E501

        :param pod_ips: The pod_ips of this V1PodStatus.  # noqa: E501
        :type pod_ips: list[V1PodIP]
        """

        self._pod_ips = pod_ips

    @property
    def qos_class(self):
        """Gets the qos_class of this V1PodStatus.  # noqa: E501

        The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#quality-of-service-classes  # noqa: E501

        :return: The qos_class of this V1PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._qos_class

    @qos_class.setter
    def qos_class(self, qos_class):
        """Sets the qos_class of this V1PodStatus.

        The Quality of Service (QOS) classification assigned to the pod based on resource requirements See PodQOSClass type for available QOS classes More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#quality-of-service-classes  # noqa: E501

        :param qos_class: The qos_class of this V1PodStatus.  # noqa: E501
        :type qos_class: str
        """

        self._qos_class = qos_class

    @property
    def reason(self):
        """Gets the reason of this V1PodStatus.  # noqa: E501

        A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted'  # noqa: E501

        :return: The reason of this V1PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1PodStatus.

        A brief CamelCase message indicating details about why the pod is in this state. e.g. 'Evicted'  # noqa: E501

        :param reason: The reason of this V1PodStatus.  # noqa: E501
        :type reason: str
        """

        self._reason = reason

    @property
    def resize(self):
        """Gets the resize of this V1PodStatus.  # noqa: E501

        Status of resources resize desired for pod's containers. It is empty if no resources resize is pending. Any changes to container resources will automatically set this to \"Proposed\"  # noqa: E501

        :return: The resize of this V1PodStatus.  # noqa: E501
        :rtype: str
        """
        return self._resize

    @resize.setter
    def resize(self, resize):
        """Sets the resize of this V1PodStatus.

        Status of resources resize desired for pod's containers. It is empty if no resources resize is pending. Any changes to container resources will automatically set this to \"Proposed\"  # noqa: E501

        :param resize: The resize of this V1PodStatus.  # noqa: E501
        :type resize: str
        """

        self._resize = resize

    @property
    def start_time(self):
        """Gets the start_time of this V1PodStatus.  # noqa: E501

        RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod.  # noqa: E501

        :return: The start_time of this V1PodStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this V1PodStatus.

        RFC 3339 date and time at which the object was acknowledged by the Kubelet. This is before the Kubelet pulled the container image(s) for the pod.  # noqa: E501

        :param start_time: The start_time of this V1PodStatus.  # noqa: E501
        :type start_time: datetime
        """

        self._start_time = start_time

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1PodStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1PodStatus):
            return True

        return self.to_dict() != other.to_dict()
