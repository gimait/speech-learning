# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pepper_command.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14pepper_command.proto\x12\x0epepper_command\x1a\x1bgoogle/protobuf/empty.proto\"M\n\x07\x43ommand\x12\x10\n\x08movement\x18\x01 \x01(\t\x12\x0b\n\x03say\x18\x02 \x01(\t\x12\x10\n\x08rotation\x18\x03 \x01(\x02\x12\x11\n\thalt_last\x18\x04 \x01(\x08\x32V\n\x06Pepper\x12L\n\x15ListenMovementCommand\x12\x16.google.protobuf.Empty\x1a\x17.pepper_command.Command\"\x00\x30\x01\x62\x06proto3')



_COMMAND = DESCRIPTOR.message_types_by_name['Command']
Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'pepper_command_pb2'
  # @@protoc_insertion_point(class_scope:pepper_command.Command)
  })
_sym_db.RegisterMessage(Command)

_PEPPER = DESCRIPTOR.services_by_name['Pepper']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMMAND._serialized_start=69
  _COMMAND._serialized_end=146
  _PEPPER._serialized_start=148
  _PEPPER._serialized_end=234
# @@protoc_insertion_point(module_scope)
