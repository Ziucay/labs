package com.app.kotlin.config

import com.app.kotlin.service.GetTimeService
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration

@Configuration
class RestConfig {

    @Bean
    fun getTimeService() : GetTimeService = GetTimeService()
}