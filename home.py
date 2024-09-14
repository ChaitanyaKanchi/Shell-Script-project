import streamlit as st
import subprocess
from concurrent.futures import ThreadPoolExecutor

def run_shell_command(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout

st.title("System Configuration")

if st.button('CPU Info'):
    with st.spinner('Fetching CPU info...'):
        output = run_shell_command("lscpu")
        st.text(output)

if st.button('Memory Info'):
    with st.spinner('Fetching Memory info...'):
        output = run_shell_command("free -h")
        st.text(output)

def run_command_async(command):
    with ThreadPoolExecutor() as executor:
        future = executor.submit(run_shell_command, command)
        return future.result()

st.title("Node Health Monitoring (Optimized)")

if st.button('Check All Health Metrics'):
    with st.spinner('Fetching node health...'):
        # Running all the health checks concurrently
        cpu_load = run_command_async("uptime | awk -F'load average:' '{ print $2 }'")
        memory_usage = run_command_async("free -h | awk '/Mem:/ {print $3 \" / \" $2}'")
        disk_usage = run_command_async("df -h / | awk 'NR==2 {print $3 \" / \" $2}'")
        network_activity = run_command_async("ifconfig | grep 'RX packets\\|TX packets'")
        top_processes = run_command_async("ps aux --sort=-%cpu | head -n 6")

        # Display results
        st.subheader("CPU Load")
        st.text(cpu_load)
        st.subheader("Memory Usage")
        st.text(memory_usage)
        st.subheader("Disk Usage")
        st.text(disk_usage)
        st.subheader("Network Activity")
        st.text(network_activity)
        st.subheader("Top 5 CPU Consuming Processes")
        st.text(top_processes)
