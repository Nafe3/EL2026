#include <stdint.h>
#include <memory>

// WeAct Blue Pill Plus: user LED on PB2 (sink / active-low)
#define RCC_BASE     0x40021000
#define GPIOB_BASE   0x40010C00
#define RCC_APB2ENR  *(volatile uint32_t *)(RCC_BASE + 0x18)
#define GPIOB_CRL    *(volatile uint32_t *)(GPIOB_BASE + 0x00)
#define GPIOB_ODR    *(volatile uint32_t *)(GPIOB_BASE + 0x0C)

#define RCC_IOPBEN (1 << 3)
#define LED_PIN    (1UL << 2)

class Led
{
private:
    bool m_ledState = false;

public:
    Led()
    {
        GPIOB_CRL &= 0xFFFFF0FF;
        GPIOB_CRL |= 0x00000200;
    }

    void TurnON()
    {
        m_ledState = true;
        GPIOB_ODR &= ~LED_PIN;
    }

    void TurnOFF()
    {
        m_ledState = false;
        GPIOB_ODR |= LED_PIN;
    }

    bool getLedState() { return m_ledState; }
};

class Timer
{
private:
    unsigned long ticks = 500000;

public:
    void sleep()
    {
        for (unsigned long i = 0; i < ticks; i++)
            ;
    }
};

int main(void)
{
    RCC_APB2ENR |= RCC_IOPBEN;
    Led m_led;
    Timer t;
    std::unique_ptr<Timer> timer{&t};

    while (1)
    {
        m_led.TurnON();
        timer->sleep();
        m_led.TurnOFF();
        timer->sleep();
    }
}
