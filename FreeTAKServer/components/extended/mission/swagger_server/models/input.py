# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.filter import Filter  # noqa: F401,E501
from swagger_server import util


class Input(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, filtergroup: List[str]=None, filter: Filter=None, auth: str=None, auth_required: bool=None, name: str=None, protocol: str=None, port: int=None, group: str=None, iface: str=None, archive: bool=None, anongroup: bool=None, archive_only: bool=None, core_version: int=None, core_version2_tls_versions: str=None):  # noqa: E501
        """Input - a model defined in Swagger

        :param filtergroup: The filtergroup of this Input.  # noqa: E501
        :type filtergroup: List[str]
        :param filter: The filter of this Input.  # noqa: E501
        :type filter: Filter
        :param auth: The auth of this Input.  # noqa: E501
        :type auth: str
        :param auth_required: The auth_required of this Input.  # noqa: E501
        :type auth_required: bool
        :param name: The name of this Input.  # noqa: E501
        :type name: str
        :param protocol: The protocol of this Input.  # noqa: E501
        :type protocol: str
        :param port: The port of this Input.  # noqa: E501
        :type port: int
        :param group: The group of this Input.  # noqa: E501
        :type group: str
        :param iface: The iface of this Input.  # noqa: E501
        :type iface: str
        :param archive: The archive of this Input.  # noqa: E501
        :type archive: bool
        :param anongroup: The anongroup of this Input.  # noqa: E501
        :type anongroup: bool
        :param archive_only: The archive_only of this Input.  # noqa: E501
        :type archive_only: bool
        :param core_version: The core_version of this Input.  # noqa: E501
        :type core_version: int
        :param core_version2_tls_versions: The core_version2_tls_versions of this Input.  # noqa: E501
        :type core_version2_tls_versions: str
        """
        self.swagger_types = {
            'filtergroup': List[str],
            'filter': Filter,
            'auth': str,
            'auth_required': bool,
            'name': str,
            'protocol': str,
            'port': int,
            'group': str,
            'iface': str,
            'archive': bool,
            'anongroup': bool,
            'archive_only': bool,
            'core_version': int,
            'core_version2_tls_versions': str
        }

        self.attribute_map = {
            'filtergroup': 'filtergroup',
            'filter': 'filter',
            'auth': 'auth',
            'auth_required': 'authRequired',
            'name': 'name',
            'protocol': 'protocol',
            'port': 'port',
            'group': 'group',
            'iface': 'iface',
            'archive': 'archive',
            'anongroup': 'anongroup',
            'archive_only': 'archiveOnly',
            'core_version': 'coreVersion',
            'core_version2_tls_versions': 'coreVersion2TlsVersions'
        }
        self._filtergroup = filtergroup
        self._filter = filter
        self._auth = auth
        self._auth_required = auth_required
        self._name = name
        self._protocol = protocol
        self._port = port
        self._group = group
        self._iface = iface
        self._archive = archive
        self._anongroup = anongroup
        self._archive_only = archive_only
        self._core_version = core_version
        self._core_version2_tls_versions = core_version2_tls_versions

    @classmethod
    def from_dict(cls, dikt) -> 'Input':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Input of this Input.  # noqa: E501
        :rtype: Input
        """
        return util.deserialize_model(dikt, cls)

    @property
    def filtergroup(self) -> List[str]:
        """Gets the filtergroup of this Input.


        :return: The filtergroup of this Input.
        :rtype: List[str]
        """
        return self._filtergroup

    @filtergroup.setter
    def filtergroup(self, filtergroup: List[str]):
        """Sets the filtergroup of this Input.


        :param filtergroup: The filtergroup of this Input.
        :type filtergroup: List[str]
        """

        self._filtergroup = filtergroup

    @property
    def filter(self) -> Filter:
        """Gets the filter of this Input.


        :return: The filter of this Input.
        :rtype: Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter: Filter):
        """Sets the filter of this Input.


        :param filter: The filter of this Input.
        :type filter: Filter
        """

        self._filter = filter

    @property
    def auth(self) -> str:
        """Gets the auth of this Input.


        :return: The auth of this Input.
        :rtype: str
        """
        return self._auth

    @auth.setter
    def auth(self, auth: str):
        """Sets the auth of this Input.


        :param auth: The auth of this Input.
        :type auth: str
        """
        allowed_values = ["LDAP", "FILE", "ANONYMOUS", "X_509"]  # noqa: E501
        if auth not in allowed_values:
            raise ValueError(
                "Invalid value for `auth` ({0}), must be one of {1}"
                .format(auth, allowed_values)
            )

        self._auth = auth

    @property
    def auth_required(self) -> bool:
        """Gets the auth_required of this Input.


        :return: The auth_required of this Input.
        :rtype: bool
        """
        return self._auth_required

    @auth_required.setter
    def auth_required(self, auth_required: bool):
        """Sets the auth_required of this Input.


        :param auth_required: The auth_required of this Input.
        :type auth_required: bool
        """

        self._auth_required = auth_required

    @property
    def name(self) -> str:
        """Gets the name of this Input.


        :return: The name of this Input.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Input.


        :param name: The name of this Input.
        :type name: str
        """

        self._name = name

    @property
    def protocol(self) -> str:
        """Gets the protocol of this Input.


        :return: The protocol of this Input.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol: str):
        """Sets the protocol of this Input.


        :param protocol: The protocol of this Input.
        :type protocol: str
        """

        self._protocol = protocol

    @property
    def port(self) -> int:
        """Gets the port of this Input.


        :return: The port of this Input.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """Sets the port of this Input.


        :param port: The port of this Input.
        :type port: int
        """

        self._port = port

    @property
    def group(self) -> str:
        """Gets the group of this Input.


        :return: The group of this Input.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group: str):
        """Sets the group of this Input.


        :param group: The group of this Input.
        :type group: str
        """

        self._group = group

    @property
    def iface(self) -> str:
        """Gets the iface of this Input.


        :return: The iface of this Input.
        :rtype: str
        """
        return self._iface

    @iface.setter
    def iface(self, iface: str):
        """Sets the iface of this Input.


        :param iface: The iface of this Input.
        :type iface: str
        """

        self._iface = iface

    @property
    def archive(self) -> bool:
        """Gets the archive of this Input.


        :return: The archive of this Input.
        :rtype: bool
        """
        return self._archive

    @archive.setter
    def archive(self, archive: bool):
        """Sets the archive of this Input.


        :param archive: The archive of this Input.
        :type archive: bool
        """

        self._archive = archive

    @property
    def anongroup(self) -> bool:
        """Gets the anongroup of this Input.


        :return: The anongroup of this Input.
        :rtype: bool
        """
        return self._anongroup

    @anongroup.setter
    def anongroup(self, anongroup: bool):
        """Sets the anongroup of this Input.


        :param anongroup: The anongroup of this Input.
        :type anongroup: bool
        """

        self._anongroup = anongroup

    @property
    def archive_only(self) -> bool:
        """Gets the archive_only of this Input.


        :return: The archive_only of this Input.
        :rtype: bool
        """
        return self._archive_only

    @archive_only.setter
    def archive_only(self, archive_only: bool):
        """Sets the archive_only of this Input.


        :param archive_only: The archive_only of this Input.
        :type archive_only: bool
        """

        self._archive_only = archive_only

    @property
    def core_version(self) -> int:
        """Gets the core_version of this Input.


        :return: The core_version of this Input.
        :rtype: int
        """
        return self._core_version

    @core_version.setter
    def core_version(self, core_version: int):
        """Sets the core_version of this Input.


        :param core_version: The core_version of this Input.
        :type core_version: int
        """

        self._core_version = core_version

    @property
    def core_version2_tls_versions(self) -> str:
        """Gets the core_version2_tls_versions of this Input.


        :return: The core_version2_tls_versions of this Input.
        :rtype: str
        """
        return self._core_version2_tls_versions

    @core_version2_tls_versions.setter
    def core_version2_tls_versions(self, core_version2_tls_versions: str):
        """Sets the core_version2_tls_versions of this Input.


        :param core_version2_tls_versions: The core_version2_tls_versions of this Input.
        :type core_version2_tls_versions: str
        """

        self._core_version2_tls_versions = core_version2_tls_versions