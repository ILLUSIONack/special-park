from job.lights import success, failure, loading

def main():
    print('Running')
    loading()
    success()
    loading()
    failure()

if __name__ == '__main__':
    main()
