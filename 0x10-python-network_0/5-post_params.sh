#!/bin/bash
#Script send a POST request to a pass URL and show the answare
curl -sX POST -d "email=test@gamil.com&subject=I will always be here for PLD" $@
