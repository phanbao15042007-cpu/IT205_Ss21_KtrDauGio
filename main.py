import logging

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


def get_shipping_rate(method: str, distance: int) -> float:
    """
    Trả về phí vận chuyển cơ sở
    """

    logger.info(
        f"Đang tính phí giao hàng cho phương thức {method} "
        f"với khoảng cách {distance} km"
    )

    # Validate khoảng cách
    if distance <= 0:
        logger.error("Distance must be positive")
        raise ValueError("Distance must be positive")

    # Xác định phí cơ sở
    if method == "standard":
        base_rate = 15000

    elif method == "express":
        base_rate = 30000

    elif method == "next_day":
        base_rate = 50000

    else:
        base_rate = 20000

    # Phụ thu đường xa
    if distance >= 20:
        base_rate += 10000

    return base_rate


def calculate_final_shipping(
    weight: float,
    distance: int,
    method: str
) -> float:
    """
    Tính tổng phí vận chuyển
    """

    if weight < 0:
        raise ValueError(
            "Trọng lượng hàng hóa không được âm"
        )

    base_rate = get_shipping_rate(
        method,
        distance
    )

    total_cost = base_rate + (weight * 2000)

    logger.warning(
        f"Kết quả: Tổng phí vận chuyển = {total_cost}"
    )

    return total_cost


if __name__ == "__main__":

    try:
        calculate_final_shipping(
            3.5,
            25,
            "express"
        )

        calculate_final_shipping(
            2.0,
            -5,
            "standard"
        )

    except ValueError as e:
        logger.error(e)