# coding: utf-8

"""
    FlashBlade Management API

    The management APIs of FlashBlade.

    OpenAPI spec version: beta

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import environment
from environment import HOST, API_TOKEN
from purity_fb import *
from utils import *


def assert_is_snapshot_list(items):
    assert type(items) is list
    for item in items:
        assert type(item) is FileSystemSnapshot


FS_A = 'rest_client_fs_for_snap_a_'
FS_B = 'rest_client_fs_for_snap_b_'
SUFFIX = 'rest-client-snap-suffix'


class TestFileSystemSnapshotsApi(unittest.TestCase):
    """ SnapshotsApi unit test stubs """

    def setUp(self):
        self.versions = environment.get_test_versions(HOST)
        self.latest = self.versions[-1]
        self.purity_fb = {}
        self.file_systems = {}
        self.snapshots = {}

        for version in self.versions:
            self.purity_fb[version] = PurityFb(HOST, version=version)
            self.purity_fb[version].disable_verify_ssl()
            res = self.purity_fb[version].login(API_TOKEN)
            self.assertTrue(res == 200)
            self.file_systems[version] = self.purity_fb[version].file_systems
            self.snapshots[version] = self.purity_fb[version].file_system_snapshots

        self.cleanUp()
        for i in range(len(self.versions)):
            fsa = FileSystem(name=FS_A + str(i))
            fsb = FileSystem(name=FS_B + str(i))
            self.file_systems[self.latest].create_file_systems(file_system=fsa)
            self.file_systems[self.latest].create_file_systems(file_system=fsb)
            suffix = SnapshotSuffix(suffix=SUFFIX)
            self.snapshots[self.latest].create_file_system_snapshots(sources=[fsa.name], suffix=suffix)
            self.snapshots[self.latest].create_file_system_snapshots(sources=[fsb.name], suffix=suffix)

    def tearDown(self):
        self.cleanUp()
        for version in self.versions:
            self.purity_fb[version].logout()

    def cleanUp(self):
        filter = 'name=\"' + FS_A + '*\" or name=\"' + FS_B + '*\"'
        res = self.file_systems[self.latest].list_file_systems(filter=filter)
        for fs in res.items:
            attr = FileSystem()
            attr.nfs = NfsRule(enabled=False)
            attr.http = ProtocolRule(enabled=False)
            attr.smb = ProtocolRule(enabled=False)
            attr.destroyed = True
            self.file_systems[self.latest].update_file_systems(name=fs.name, attributes=attr)
            self.file_systems[self.latest].delete_file_systems(name=fs.name)
            # deleting a file system will delete its snapshots
            # so no need to clean up snapshots

    def test_create(self):
        """
        Test case for create
        """
        i = 0
        for version in self.versions:
            source = FS_A + str(i)
            i += 1
            response = self.snapshots[version].create_file_system_snapshots(sources=[source])
            assert type(response) is FileSystemSnapshotResponse
            assert_is_snapshot_list(response.items)
            assert len(response.items) == 1
            assert response.items[0].source == source

            suffix = "snap-by-sdk"
            response = self.snapshots[version].create_file_system_snapshots(sources=[source],
                                                                            suffix=SnapshotSuffix(suffix=suffix))
            assert type(response) is FileSystemSnapshotResponse
            assert_is_snapshot_list(response.items)
            assert len(response.items) == 1
            assert response.items[0].source == source
            assert response.items[0].suffix == suffix

    def test_update(self):
        """
        Test case for create
        """
        i = 0
        for version in self.versions:
            source = FS_A + str(i)
            name = source + "." + SUFFIX
            i += 1
            snap_attr = FileSystemSnapshot(destroyed=True)
            try:
                response = self.snapshots[version].update_file_system_snapshots(name=name, attributes=snap_attr)
                assert type(response) is FileSystemSnapshotResponse
                assert_is_snapshot_list(response.items)
                assert len(response.items) == 1
                assert response.items[0].source == source
                assert response.items[0].destroyed
            except AttributeError as err:
                assert version == '1.0'

    def test_list(self):
        """
        Test case for list
        """
        i = 0
        for version in self.versions:
            source_a = FS_A + str(i)
            source_b = FS_A + str(i)
            i += 1

            response = self.snapshots[version].list_file_system_snapshots(names_or_sources=[source_a])
            assert type(response) is FileSystemSnapshotResponse
            assert_is_snapshot_list(response.items)
            for snapshot in response.items:
                assert snapshot.source == source_a
                assert snapshot.name.startswith(source_a + '.')

            snap_name = "%s.%s" % (source_b, SUFFIX)
            response = self.snapshots[version].list_file_system_snapshots(names_or_sources=[source_b, snap_name])
            assert type(response) is FileSystemSnapshotResponse
            assert_is_snapshot_list(response.items)
            for snapshot in response.items:
                assert snapshot.name == snap_name or snapshot.source == source_b


if __name__ == '__main__':
    unittest.main()
