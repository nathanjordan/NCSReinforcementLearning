#!/usr/bin/sh
rm -rf VOLTAGE.* && rm -rf sim.out
applications/ncsDistributor/ncsDistributor reinforcement.in cluster.out sim.out
applications/simulator/simulator sim.out
