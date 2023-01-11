def logging(Time, Sender, Data, Result):
    Result = Result.split('\n')
    with open('log.csv', 'a') as file:
        file.write(f"{Time};{Sender};{Data};{' '.join(Result)}\n")
