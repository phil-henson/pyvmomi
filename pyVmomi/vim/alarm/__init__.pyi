from typing import List
from enum import Enum
from pyVmomi import vim, vmodl
from datetime import datetime
from pyVmomi.VmomiSupport import ManagedObject, NoneType, PropertyPath


class Alarm(vim.ExtensibleManagedObject):
    @property
    def info(self) -> AlarmInfo: ...
    def Remove(self) -> NoneType: ...
    def Reconfigure(self, spec: AlarmSpec) -> NoneType: ...


class AlarmManager(ManagedObject):
    @property
    def defaultExpression(self) -> List[AlarmExpression]: ...
    @property
    def description(self) -> AlarmDescription: ...
    def Create(self, entity: vim.ManagedEntity, spec: AlarmSpec) -> Alarm: ...
    def GetAlarm(self, entity: vim.ManagedEntity) -> List[Alarm]: ...
    def GetAlarmActionsEnabled(self, entity: vim.ManagedEntity) -> bool: ...
    def SetAlarmActionsEnabled(self, entity: vim.ManagedEntity, enabled: bool) -> NoneType: ...
    def GetAlarmState(self, entity: vim.ManagedEntity) -> List[AlarmState]: ...
    def AcknowledgeAlarm(self, alarm: Alarm, entity: vim.ManagedEntity) -> NoneType: ...
    def ClearTriggeredAlarms(self, filter: AlarmFilterSpec) -> NoneType: ...
    def DisableAlarm(self, alarm: Alarm, entity: vim.ManagedEntity) -> NoneType: ...
    def EnableAlarm(self, alarm: Alarm, entity: vim.ManagedEntity) -> NoneType: ...


class AlarmAction(vmodl.DynamicData): ...


class AlarmDescription(vmodl.DynamicData):
    @property
    def expr(self) -> List[vim.TypeDescription]: ...
    @property
    def stateOperator(self) -> List[vim.ElementDescription]: ...
    @property
    def metricOperator(self) -> List[vim.ElementDescription]: ...
    @property
    def hostSystemConnectionState(self) -> List[vim.ElementDescription]: ...
    @property
    def virtualMachinePowerState(self) -> List[vim.ElementDescription]: ...
    @property
    def datastoreConnectionState(self) -> List[vim.ElementDescription]: ...
    @property
    def hostSystemPowerState(self) -> List[vim.ElementDescription]: ...
    @property
    def virtualMachineGuestHeartbeatStatus(self) -> List[vim.ElementDescription]: ...
    @property
    def entityStatus(self) -> List[vim.ElementDescription]: ...
    @property
    def action(self) -> List[vim.TypeDescription]: ...


class AlarmExpression(vmodl.DynamicData): ...


class AlarmFilterSpec(vmodl.DynamicData):
    @property
    def status(self) -> List[vim.ManagedEntity.Status]: ...
    @property
    def typeEntity(self) -> str: ...
    @property
    def typeTrigger(self) -> str: ...


    class AlarmTypeByEntity(Enum):
        entityTypeAll = "entitytypeall"
        entityTypeHost = "entitytypehost"
        entityTypeVm = "entitytypevm"


    class AlarmTypeByTrigger(Enum):
        triggerTypeAll = "triggertypeall"
        triggerTypeEvent = "triggertypeevent"
        triggerTypeMetric = "triggertypemetric"


class AlarmInfo(AlarmSpec):
    @property
    def key(self) -> str: ...
    @property
    def alarm(self) -> Alarm: ...
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @property
    def lastModifiedTime(self) -> datetime: ...
    @property
    def lastModifiedUser(self) -> str: ...
    @property
    def creationEventId(self) -> int: ...


class AlarmSetting(vmodl.DynamicData):
    @property
    def toleranceRange(self) -> int: ...
    @property
    def reportingFrequency(self) -> int: ...


class AlarmSpec(vmodl.DynamicData):
    @property
    def name(self) -> str: ...
    @property
    def systemName(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def enabled(self) -> bool: ...
    @property
    def expression(self) -> AlarmExpression: ...
    @property
    def action(self) -> AlarmAction: ...
    @property
    def actionFrequency(self) -> int: ...
    @property
    def setting(self) -> AlarmSetting: ...


class AlarmState(vmodl.DynamicData):
    @property
    def key(self) -> str: ...
    @property
    def entity(self) -> vim.ManagedEntity: ...
    @property
    def alarm(self) -> Alarm: ...
    @property
    def overallStatus(self) -> vim.ManagedEntity.Status: ...
    @property
    def time(self) -> datetime: ...
    @property
    def acknowledged(self) -> bool: ...
    @property
    def acknowledgedByUser(self) -> str: ...
    @property
    def acknowledgedTime(self) -> datetime: ...
    @property
    def eventKey(self) -> int: ...
    @property
    def disabled(self) -> bool: ...


class AlarmTriggeringAction(AlarmAction):
    @property
    def action(self) -> vim.action.Action: ...
    @property
    def transitionSpecs(self) -> List[AlarmTriggeringAction.TransitionSpec]: ...
    @property
    def green2yellow(self) -> bool: ...
    @property
    def yellow2red(self) -> bool: ...
    @property
    def red2yellow(self) -> bool: ...
    @property
    def yellow2green(self) -> bool: ...


    class TransitionSpec(vmodl.DynamicData):
        @property
        def startState(self) -> vim.ManagedEntity.Status: ...
        @property
        def finalState(self) -> vim.ManagedEntity.Status: ...
        @property
        def repeats(self) -> bool: ...


class AndAlarmExpression(AlarmExpression):
    @property
    def expression(self) -> List[AlarmExpression]: ...


class EventAlarmExpression(AlarmExpression):
    @property
    def comparisons(self) -> List[EventAlarmExpression.Comparison]: ...
    @property
    def eventType(self) -> type: ...
    @property
    def eventTypeId(self) -> str: ...
    @property
    def objectType(self) -> type: ...
    @property
    def status(self) -> vim.ManagedEntity.Status: ...


    class Comparison(vmodl.DynamicData):
        @property
        def attributeName(self) -> str: ...
        @property
        def operator(self) -> str: ...
        @property
        def value(self) -> str: ...


    class ComparisonOperator(Enum):
        equals = "equals"
        notEqualTo = "notequalto"
        startsWith = "startswith"
        doesNotStartWith = "doesnotstartwith"
        endsWith = "endswith"
        doesNotEndWith = "doesnotendwith"


class GroupAlarmAction(AlarmAction):
    @property
    def action(self) -> List[AlarmAction]: ...


class MetricAlarmExpression(AlarmExpression):
    @property
    def operator(self) -> MetricAlarmExpression.MetricOperator: ...
    @property
    def type(self) -> type: ...
    @property
    def metric(self) -> vim.PerformanceManager.MetricId: ...
    @property
    def yellow(self) -> int: ...
    @property
    def yellowInterval(self) -> int: ...
    @property
    def red(self) -> int: ...
    @property
    def redInterval(self) -> int: ...


    class MetricOperator(Enum):
        isAbove = "isabove"
        isBelow = "isbelow"


class OrAlarmExpression(AlarmExpression):
    @property
    def expression(self) -> List[AlarmExpression]: ...


class StateAlarmExpression(AlarmExpression):
    @property
    def operator(self) -> StateAlarmExpression.StateOperator: ...
    @property
    def type(self) -> type: ...
    @property
    def statePath(self) -> PropertyPath: ...
    @property
    def yellow(self) -> str: ...
    @property
    def red(self) -> str: ...


    class StateOperator(Enum):
        isEqual = "isequal"
        isUnequal = "isunequal"