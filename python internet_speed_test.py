import speedtest


def get_speed():
    st = speedtest.Speedtest()

    # Get download speed in bits per second
    download_speed = st.download()

    # Get upload speed in bits per second
    upload_speed = st.upload()

    # Convert speeds to Mbps
    download_speed_mbps = download_speed / 10 ** 6
    upload_speed_mbps = upload_speed / 10 ** 6

    return download_speed_mbps, upload_speed_mbps


def display_results(download_speed, upload_speed):
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")


def main():
    print("Running Internet Speed Test...")
    download_speed, upload_speed = get_speed()
    print("\nSpeed Test Results:")
    display_results(download_speed, upload_speed)


if __name__ == "__main__":
    main()
