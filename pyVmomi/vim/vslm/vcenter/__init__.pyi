from typing import List
from pyVmomi import vim, vmodl
from pyVmomi.VmomiSupport import NoneType, long


class VStorageObjectManager(vim.vslm.VStorageObjectManagerBase):
    def CreateDisk(self, spec: vim.vslm.CreateSpec) -> vim.Task: ...
    def RegisterDisk(self, path: str, name: str) -> vim.vslm.VStorageObject: ...
    def ExtendDisk(self, id: vim.vslm.ID, datastore: vim.Datastore, newCapacityInMB: long) -> vim.Task: ...
    def InflateDisk(self, id: vim.vslm.ID, datastore: vim.Datastore) -> vim.Task: ...
    def RenameVStorageObject(self, id: vim.vslm.ID, datastore: vim.Datastore, name: str) -> NoneType: ...
    def UpdateVStorageObjectPolicy(self, id: vim.vslm.ID, datastore: vim.Datastore, profile: List[vim.vm.ProfileSpec]) -> vim.Task: ...
    def UpdateVStorageObjectCrypto(self, id: vim.vslm.ID, datastore: vim.Datastore, profile: List[vim.vm.ProfileSpec], disksCrypto: vim.vslm.DiskCryptoSpec) -> vim.Task: ...
    def UpdateVStorageInfrastructureObjectPolicy(self, spec: vim.vslm.InfrastructureObjectPolicySpec) -> vim.Task: ...
    def RetrieveVStorageInfrastructureObjectPolicy(self, datastore: vim.Datastore) -> List[vim.vslm.InfrastructureObjectPolicy]: ...
    def DeleteVStorageObject(self, id: vim.vslm.ID, datastore: vim.Datastore) -> vim.Task: ...
    def RetrieveVStorageObject(self, id: vim.vslm.ID, datastore: vim.Datastore, diskInfoFlags: List[str]) -> vim.vslm.VStorageObject: ...
    def RetrieveVStorageObjectState(self, id: vim.vslm.ID, datastore: vim.Datastore) -> vim.vslm.StateInfo: ...
    def RetrieveVStorageObjectAssociations(self, ids: List[RetrieveVStorageObjSpec]) -> List[VStorageObjectAssociations]: ...
    def ListVStorageObject(self, datastore: vim.Datastore) -> List[vim.vslm.ID]: ...
    def CloneVStorageObject(self, id: vim.vslm.ID, datastore: vim.Datastore, spec: vim.vslm.CloneSpec) -> vim.Task: ...
    def RelocateVStorageObject(self, id: vim.vslm.ID, datastore: vim.Datastore, spec: vim.vslm.RelocateSpec) -> vim.Task: ...
    def SetVStorageObjectControlFlags(self, id: vim.vslm.ID, datastore: vim.Datastore, controlFlags: List[str]) -> NoneType: ...
    def ClearVStorageObjectControlFlags(self, id: vim.vslm.ID, datastore: vim.Datastore, controlFlags: List[str]) -> NoneType: ...
    def AttachTagToVStorageObject(self, id: vim.vslm.ID, category: str, tag: str) -> NoneType: ...
    def DetachTagFromVStorageObject(self, id: vim.vslm.ID, category: str, tag: str) -> NoneType: ...
    def ListVStorageObjectsAttachedToTag(self, category: str, tag: str) -> List[vim.vslm.ID]: ...
    def ListTagsAttachedToVStorageObject(self, id: vim.vslm.ID) -> List[vim.vslm.TagEntry]: ...
    def ReconcileDatastoreInventory(self, datastore: vim.Datastore) -> vim.Task: ...
    def ScheduleReconcileDatastoreInventory(self, datastore: vim.Datastore) -> NoneType: ...
    def CreateSnapshot(self, id: vim.vslm.ID, datastore: vim.Datastore, description: str) -> vim.Task: ...
    def DeleteSnapshot(self, id: vim.vslm.ID, datastore: vim.Datastore, snapshotId: vim.vslm.ID) -> vim.Task: ...
    def RetrieveSnapshotInfo(self, id: vim.vslm.ID, datastore: vim.Datastore) -> vim.vslm.VStorageObjectSnapshotInfo: ...
    def CreateDiskFromSnapshot(self, id: vim.vslm.ID, datastore: vim.Datastore, snapshotId: vim.vslm.ID, name: str, profile: List[vim.vm.ProfileSpec], crypto: vim.encryption.CryptoSpec, path: str) -> vim.Task: ...
    def RevertVStorageObject(self, id: vim.vslm.ID, datastore: vim.Datastore, snapshotId: vim.vslm.ID) -> vim.Task: ...
    def RetrieveSnapshotDetails(self, id: vim.vslm.ID, datastore: vim.Datastore, snapshotId: vim.vslm.ID) -> vim.vslm.VStorageObjectSnapshotDetails: ...
    def QueryChangedDiskAreas(self, id: vim.vslm.ID, datastore: vim.Datastore, snapshotId: vim.vslm.ID, startOffset: long, changeId: str) -> vim.VirtualMachine.DiskChangeInfo: ...
    def DeleteVStorageObjectEx(self, id: vim.vslm.ID, datastore: vim.Datastore) -> vim.Task: ...
    def UpdateVStorageObjectMetadataEx(self, id: vim.vslm.ID, datastore: vim.Datastore, metadata: List[vim.KeyValue], deleteKeys: List[str]) -> vim.Task: ...


class RetrieveVStorageObjSpec(vmodl.DynamicData):
    @property
    def id(self) -> vim.vslm.ID: ...
    @property
    def datastore(self) -> vim.Datastore: ...


class VStorageObjectAssociations(vmodl.DynamicData):
    @property
    def id(self) -> vim.vslm.ID: ...
    @property
    def vmDiskAssociations(self) -> List[VStorageObjectAssociations.VmDiskAssociations]: ...
    @property
    def fault(self) -> vmodl.MethodFault: ...


    class VmDiskAssociations(vmodl.DynamicData):
        @property
        def vmId(self) -> str: ...
        @property
        def diskKey(self) -> int: ...