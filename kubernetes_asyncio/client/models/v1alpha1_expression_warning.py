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


class V1alpha1ExpressionWarning(object):
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
        'field_ref': 'str',
        'warning': 'str'
    }

    attribute_map = {
        'field_ref': 'fieldRef',
        'warning': 'warning'
    }

    def __init__(self, field_ref=None, warning=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1ExpressionWarning - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._field_ref = None
        self._warning = None
        self.discriminator = None

        self.field_ref = field_ref
        self.warning = warning

    @property
    def field_ref(self):
        """Gets the field_ref of this V1alpha1ExpressionWarning.  # noqa: E501

        The path to the field that refers the expression. For example, the reference to the expression of the first item of validations is \"spec.validations[0].expression\"  # noqa: E501

        :return: The field_ref of this V1alpha1ExpressionWarning.  # noqa: E501
        :rtype: str
        """
        return self._field_ref

    @field_ref.setter
    def field_ref(self, field_ref):
        """Sets the field_ref of this V1alpha1ExpressionWarning.

        The path to the field that refers the expression. For example, the reference to the expression of the first item of validations is \"spec.validations[0].expression\"  # noqa: E501

        :param field_ref: The field_ref of this V1alpha1ExpressionWarning.  # noqa: E501
        :type field_ref: str
        """
        if self.local_vars_configuration.client_side_validation and field_ref is None:  # noqa: E501
            raise ValueError("Invalid value for `field_ref`, must not be `None`")  # noqa: E501

        self._field_ref = field_ref

    @property
    def warning(self):
        """Gets the warning of this V1alpha1ExpressionWarning.  # noqa: E501

        The content of type checking information in a human-readable form. Each line of the warning contains the type that the expression is checked against, followed by the type check error from the compiler.  # noqa: E501

        :return: The warning of this V1alpha1ExpressionWarning.  # noqa: E501
        :rtype: str
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this V1alpha1ExpressionWarning.

        The content of type checking information in a human-readable form. Each line of the warning contains the type that the expression is checked against, followed by the type check error from the compiler.  # noqa: E501

        :param warning: The warning of this V1alpha1ExpressionWarning.  # noqa: E501
        :type warning: str
        """
        if self.local_vars_configuration.client_side_validation and warning is None:  # noqa: E501
            raise ValueError("Invalid value for `warning`, must not be `None`")  # noqa: E501

        self._warning = warning

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
        if not isinstance(other, V1alpha1ExpressionWarning):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1ExpressionWarning):
            return True

        return self.to_dict() != other.to_dict()
