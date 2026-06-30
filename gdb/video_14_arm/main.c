#include <stdint.h>

// WeAct Blue Pill Plus: user LED on PB2 (sink / active-low)
#define RCC_BASE     0x40021000
#define GPIOB_BASE   0x40010C00
#define RCC_APB2ENR  *(volatile uint32_t *)(RCC_BASE + 0x18)
#define GPIOB_CRL    *(volatile uint32_t *)(GPIOB_BASE + 0x00)
#define GPIOB_ODR    *(volatile uint32_t *)(GPIOB_BASE + 0x0C)

#define RCC_IOPBEN (1 << 3)
#define LED_PIN    (1UL << 2)

int main(void)
{
	RCC_APB2ENR |= RCC_IOPBEN;
	GPIOB_CRL   &= 0xFFFFF0FF;
	GPIOB_CRL   |= 0x00000200;

	while (1)
	{
		GPIOB_ODR &= ~LED_PIN;
		for (int i = 0; i < 500000; i++);

		GPIOB_ODR |= LED_PIN;
		for (int i = 0; i < 500000; i++);
	}
}
