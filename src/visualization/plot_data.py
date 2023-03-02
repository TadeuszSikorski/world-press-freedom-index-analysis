from plotnine import ggplot, aes, geom_histogram, geom_density


def plot_histogram_and_density(df, column, file_path):
    plot = (ggplot(df, aes(x=column))
            + geom_histogram(binwidth=1, color="black", fill="white")
            + geom_density(color="red"))
    
    plot.save(filename=file_path, dpi=300)
