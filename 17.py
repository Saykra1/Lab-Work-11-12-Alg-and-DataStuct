class TreeNode:
    """Класс для представления узла бинарного дерева"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_leaves(root):
    """
    Рекурсивная функция для подсчета количества листьев в бинарном дереве.
    Лист - это узел, у которого нет потомков (ни левого, ни правого).
    """
    if root is None:
        return 0

    # Если узел не имеет потомков - это лист
    if root.left is None and root.right is None:
        return 1

    # Рекурсивно подсчитываем листья в левом и правом поддеревьях
    return count_leaves(root.left) + count_leaves(root.right)


# Альтернативная версия с подробными комментариями
def count_leaves_detailed(root):
    """
    Более подробная версия с явной обработкой случаев.
    """
    # Базовый случай: пустое дерево
    if root is None:
        return 0

    # Базовый случай: узел является листом
    if root.left is None and root.right is None:
        return 1

    # Рекурсивный случай: узел имеет потомков
    left_leaves = count_leaves_detailed(root.left)
    right_leaves = count_leaves_detailed(root.right)

    return left_leaves + right_leaves


# Функция для создания дерева из списка (для тестирования)
def build_tree_from_list(lst, index=0):
    """
    Создает бинарное дерево из списка (в формате heap-like).
    None представляет отсутствующий узел.
    """
    if index >= len(lst) or lst[index] is None:
        return None

    root = TreeNode(lst[index])
    root.left = build_tree_from_list(lst, 2 * index + 1)
    root.right = build_tree_from_list(lst, 2 * index + 2)

    return root


# Примеры использования и тестирования
if __name__ == "__main__":
    # Пример 1: Простое дерево
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)
    tree1.left.left = TreeNode(4)
    tree1.left.right = TreeNode(5)

    print("Пример 1:")
    print(f"Количество листьев: {count_leaves(tree1)}")  # Должно быть 3

    # Пример 2: Дерево с одним узлом
    #     1
    tree2 = TreeNode(1)
    print("\nПример 2:")
    print(f"Количество листьев: {count_leaves(tree2)}")  # Должно быть 1

    # Пример 3: Пустое дерево
    tree3 = None
    print("\nПример 3:")
    print(f"Количество листьев: {count_leaves(tree3)}")  # Должно быть 0

    # Пример 4: Сбалансированное дерево
    #       1
    #      / \
    #     2   3
    #    / \ / \
    #   4  5 6  7
    tree4 = build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    print("\nПример 4:")
    print(f"Количество листьев: {count_leaves(tree4)}")  # Должно быть 4

    # Пример 5: Несбалансированное дерево
    #       1
    #      / \
    #     2   3
    #    /   / \
    #   4   5   6
    #        \
    #         7
    tree5 = TreeNode(1)
    tree5.left = TreeNode(2)
    tree5.right = TreeNode(3)
    tree5.left.left = TreeNode(4)
    tree5.right.left = TreeNode(5)
    tree5.right.right = TreeNode(6)
    tree5.right.left.right = TreeNode(7)

    print("\nПример 5:")
    print(f"Количество листьев: {count_leaves(tree5)}")  # Должно быть 4


# Дополнительная функция для визуализации дерева (опционально)
def print_tree(root, level=0, prefix="Root: "):
    """Рекурсивно выводит структуру дерева"""
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")