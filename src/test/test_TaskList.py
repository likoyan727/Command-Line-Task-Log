import pytest

def test_add_urgent_task():
  file_writer = open("test_urgent_list.txt", mode="a")
  file_writer.write("Test task")
  file_writer.write("Second test")
  file_writer.close()

  file_reader = open("test_urgent_list.txt", mode='r')
  line = file_reader.read()
  assert line == "Second test"








