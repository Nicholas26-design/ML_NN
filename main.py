from run_pipeline import install_requirements, preprocess_data, analyze_data

if __name__ == "__main__":
    try:
        install_requirements()
        preprocess_data()
        analyze_data()
        print("Pipeline execution completed successfully.")
    except RuntimeError as e:
        print(f"Pipeline execution failed: {e}")

