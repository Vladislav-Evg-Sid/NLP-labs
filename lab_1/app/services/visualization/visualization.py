import matplotlib.pyplot as plt
from wordcloud import WordCloud
from typing import Optional
import multiprocessing as mp


def create_hist(freqs: dict[str, int], count_words_to_visualization: int = 20, ax: Optional[plt.Axes] = None) -> None:
    """Визуализаци гистограммы частотности токенов

    Args:
        freqs (dict[str, int]): Словарь токен - количество
        count_words_to_visualization (int, optional): Топ n токенов для визуализации. Defaults to 20.
        ax (Optional[plt.Axes], optional): Полотно для визуализации. Defaults to None.
    """    
    sorted_items = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
    words = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]

    created_fig = False
    if ax is None:
        created_fig = True
        fig, ax = plt.subplots(figsize=(12, 6))

    ax.bar(words[:count_words_to_visualization], counts[:count_words_to_visualization], color='skyblue', edgecolor='navy')
    ax.set_xlabel('Токены', fontsize=12)
    ax.set_ylabel('Частота', fontsize=12)
    ax.set_title('Гистограмма частоты токенов', fontsize=14)
    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_ha('right')

    if created_fig:
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.1)


def create_wordcloud(freqs: dict[str, int], count_words_to_visualization: int = 20, ax: Optional[plt.Axes] = None) -> None:
    """Визуализация облака слов

    Args:
        freqs (dict[str, int]): Словарь токен - количество
        count_words_to_visualization (int, optional): Топ n токенов для визуализации. Defaults to 20.
        ax (Optional[plt.Axes], optional): Полотно для визуализации. Defaults to None.
    """    
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        max_words=count_words_to_visualization,
        max_font_size=100,
        min_font_size=10,
        colormap='viridis',
        random_state=42
    ).generate_from_frequencies(freqs)

    created_fig = False
    if ax is None:
        created_fig = True
        fig, ax = plt.subplots(figsize=(12, 6))

    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Облако токенов', fontsize=16)

    if created_fig:
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.1)


def _show_both_process(
    freqs: dict[str, int],
    count_words_to_visualization_hist: int = 20,
    count_words_to_visualization_wc: int = 40,
    window_name: str = "Анализ токенов",
) -> None:
    """Отдельный процесс для визуализации паралельно обработке

    Args:
        freqs (dict[str, int]): Словарь токен - количество
        count_words_to_visualization_hist (int, optional): Топ n токенов для визуализации гистограммы. Defaults to 20.
        count_words_to_visualization_wc (int, optional): Топ n токенов для визуализации облака слов. Defaults to 40.
        window_name (str, optional): Название окна. Defaults to "Анализ токенов".
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    create_hist(freqs, count_words_to_visualization=count_words_to_visualization_hist, ax=axes[0])
    create_wordcloud(freqs, count_words_to_visualization=count_words_to_visualization_wc, ax=axes[1])

    try:
        fig.canvas.manager.set_window_title(window_name)
    except Exception:
        pass

    plt.tight_layout()
    plt.show()


def create_both(
    freqs: dict[str, int],
    count_words_to_visualization_hist: int = 20,
    count_words_to_visualization_wc: int = 40,
    window_name: str = "Анализ токенов",
) -> mp.Process:
    """Визуализация графиков

    Args:
        freqs (dict[str, int]): Словарь токен - количество
        count_words_to_visualization_hist (int, optional): Топ n токенов для визуализации гистограммы. Defaults to 20.
        count_words_to_visualization_wc (int, optional): Топ n токенов для визуализации облака слов. Defaults to 40.
        window_name (str, optional): Название окна. Defaults to "Анализ токенов".

    Returns:
        mp.Process: Процесс
    """    
    p = mp.Process(
        target=_show_both_process,
        args=(freqs, count_words_to_visualization_hist, count_words_to_visualization_wc, window_name),
    )
    p.daemon = True
    p.start()
    return p