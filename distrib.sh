#!/bin/bash

case "$1" in
  build)
	tar -czvf flask_hello.tar.gz flask_hello
	;;
esac
