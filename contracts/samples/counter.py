from pyteal import *
from pyteal.ast.bytes import Bytes
from pyteal_helpers import program

UINT64_MAX = 0xffffffffffffffff

def approval():
	# Global variables
	global_owner = Bytes("owner")  # byteslice
	global_counter = Bytes("counter")  # uint64

	# Scratch variables
	scratch_counter = ScratchVar(TealType.uint64)

	# Operations
	op_increment = Bytes("inc")
	op_decrement = Bytes("dec")


	@Subroutine(TealType.none)
	def increment():
		return Seq(
			[
				scratch_counter.store(App.globalGet(global_counter)),
				# Detect overflow
				If(scratch_counter.load() < Int(UINT64_MAX))
				.Then(App.globalPut(global_counter, scratch_counter.load() + Int(1))),
				Approve(),
			]
		)

	@Subroutine(TealType.none)
	def decrement():
		return Seq(
			[
				scratch_counter.store(App.globalGet(global_counter)),
				# Detect underflow
				If(scratch_counter.load() > Int(0))
				.Then(App.globalPut(global_counter, scratch_counter.load() - Int(1))),
				Approve(),
			]
		)

	return program.event(
		init=Seq(
			[
				App.globalPut(global_owner, Txn.sender()),
				App.globalPut(global_counter, Int(0)),
				Approve(),
			]
		),
		no_op=Cond(
			[Txn.application_args[0] == op_increment, increment()],
			[Txn.application_args[0] == op_decrement, increment()],
		),
	)


def clear():
	return Approve()
