import import_games_hokej
import checking_data_hokej
import import_games_alpe
import checking_data_alpe

# Your main function or sequence of calls
if __name__ == "__main__":
    print("Running import_games_hokej.py...")
    import_games_hokej.main() 
    print("Completed import_games_hokej.py\n")

    print("Running checking_data_hokej.py...")
    checking_data_hokej.main()
    print("Completed checking_data_hokej.py\n")

    print("Running import_games_alpe.py...")
    import_games_alpe.main()
    print("Completed import_games_alpe.py\n")

    print("Running checking_data_alpe.py...")
    checking_data_alpe.main()
    print("Completed checking_data_alpe.py")